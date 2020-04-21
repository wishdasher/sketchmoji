import math
import numpy as np
import scipy.io
import matplotlib.pyplot as plt
from matplotlib import patches

from detect_peaks import detect_peaks
from circle_fit import circle_fit

# If matplotlib is not working on OSX follow directions in the link below
# https://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python


# parameters - original values
PEN_SMOOTHING_WINDOW = 5
TANGENT_WINDOW = 11
CURVATURE_WINDOW = 11
SPEED_THRESHOLD_1 = .25 #a percentage of the average speed
CURVATURE_THRESHOLD = .75 #in degrees per pixel
SPEED_THRESHOLD_2 = .80 #a percentage of the average speed
MINIMUM_DISTANCE_BETWEEN_CORNERS = 0
MINIMUM_ARC_ANGLE = 36 #in degrees
MERGE_LENGTH_THRESHOLD = .2
MERGE_FIT_ERROR_THRESHOLD = .1

# redefining here to be my values
# goto
PEN_SMOOTHING_WINDOW = 5
TANGENT_WINDOW = 11
CURVATURE_WINDOW = 11
SPEED_THRESHOLD_1 = .25 #a percentage of the average speed
CURVATURE_THRESHOLD = .75 #in degrees per pixel
SPEED_THRESHOLD_2 = .80 #a percentage of the average speed
MINIMUM_DISTANCE_BETWEEN_CORNERS = 50
MINIMUM_ARC_ANGLE = 36 #in degrees
MERGE_LENGTH_THRESHOLD = .2
MERGE_FIT_ERROR_THRESHOLD = 1


def compute_cumulative_arc_lengths(stroke):
    """
    param stroke : a Stroke object with N x,y,t data points

    return : the array (length N) of the cumulative arc lengths between each pair
        of consecutive sampled points in a stroke of length N.
    """
    if len(stroke.x) == 0:
        return []

    arc_lengths = [math.hypot(
        stroke.x[i + 1] - stroke.x[i],
        stroke.y[i + 1] - stroke.y[i]
        ) for i in range(len(stroke.x) - 1)]

    cum_length = 0
    cum_lengths = [0]
    for al in arc_lengths:
        cum_length += al
        cum_lengths.append(cum_length)

    return cum_lengths

def get_smoothing_indices(index, n, window):
    offset = (window - 1) / 2
    return (max(0, math.floor(index - offset)),
        min(n - 1, math.floor(index + offset)))

def compute_smoothed_pen_speeds(stroke, cumulative_arc_lengths,
    window=PEN_SMOOTHING_WINDOW):
    """
    param stroke : a Stroke object with N x,y,t data points
    param cumulative_arc_lengths : array of the cumulative arc lengths of the
        stroke
    param window : size of the window over which smoothing occurs

    return : an array (length N) of the smoothed pen speeds at each point on
        a stroke of length N.
    """
    n = len(stroke.t)

    speeds = [0]
    for i in range(1, n - 1):
        dt = (stroke.t[i + 1] - stroke.t[i - 1])
        vx = (stroke.x[i + 1] - stroke.x[i - 1]) / dt
        vy = (stroke.y[i + 1] - stroke.y[i - 1]) / dt
        speeds.append(math.hypot(vx, vy))
    # adjust first and last values
    speeds[0] = speeds[1]
    speeds.append(speeds[-1])
    assert len(stroke.t) == len(speeds)

    smoothed_speeds = []
    for i in range(n):
        index_left, index_right = get_smoothing_indices(i, n, window)
        window_speeds = speeds[index_left : index_right + 1]
        smoothed_speeds.append(sum(window_speeds) / len(window_speeds))

    return smoothed_speeds

def compute_tangents(stroke, window=TANGENT_WINDOW):
    """
    param stroke : a Stroke object with N x,y,t data points
    param window : size of the window over which you calculate the regression

    return : an array (length N) of tangents
    """
    n = len(stroke.t)

    tangents = []
    for i in range(n):
        index_left, index_right = get_smoothing_indices(i, n, window)
        xs = stroke.x[index_left : index_right + 1]
        ys = stroke.y[index_left : index_right + 1]
        m, b = np.polyfit(xs, ys, 1)
        tangents.append(m)

    return tangents

def compute_angles(stroke, tangents):
    """
    param stroke : a Stroke object with N x,y,t data points
    param tangents : an array of tangents (length N)

    return : an array of angles (length N)
    """

    #TODO: is there more to this?
    return [math.atan(x) for x in tangents]

def plot_angles(stroke, angles):
    """
    param stroke : a Stroke object with N x,y,t data points
    param angles : an array of angles

    return : nothing (but should show a plot)
    """
    plt.plot(angles)
    plt.show()
    return

def correct_angles(stroke, angles):
    """
    param stroke : a Stroke object with N x,y,t data points
    param angles : an array of angles (length N)

    return : an array of angles (length N) correcting for the phenomenon you find
    """
    correction_threshold = math.pi * .5
    bad_angles = angles
    good_angles = []
    adj = 0
    for i in range(len(bad_angles)):
        if i != 0 and abs(bad_angles[i] - bad_angles[i - 1]) > correction_threshold:
            adj += (math.pi if bad_angles[i] < bad_angles[i - 1] else -math.pi)
        good_angles.append(bad_angles[i] + adj)

    return good_angles

def compute_curvatures(stroke, cumulative_arc_lengths, angles,
    curvature_window=CURVATURE_WINDOW):
    """
    param stroke : a Stroke object with N x,y,t data points
    param cumulative_arc_lengths : an array of the cumulative arc lengths of a stroke
    param angles : an array of angles
    param curvature_window : size of the window over which you calculate the least squares line

    return : an array of curvatures
    """

    assert len(cumulative_arc_lengths) == len(angles)
    n = len(cumulative_arc_lengths)

    curvatures = []
    for i in range(n):
        index_left, index_right = get_smoothing_indices(i, n, curvature_window)
        ys = cumulative_arc_lengths[index_left : index_right + 1]
        xs = angles[index_left : index_right + 1]
        filtered_xs = [xs[0]]
        filtered_ys = [ys[0]]
        for j in range(1, len(ys)):
            if ys[j] - ys[j-1] > 0.01:
                filtered_xs.append(xs[j])
                filtered_ys.append(ys[j])
        m, b = np.polyfit(filtered_xs, filtered_ys, 1)
        curvatures.append(m)

    return curvatures

def compute_corners_using_speed_alone(stroke, smoothed_pen_speeds,
    speed_threshold_1=SPEED_THRESHOLD_1):
    """
    param stroke : a Stroke object with N x,y,t data points
    param smoothed_pen_speeds : an array of the smoothed pen speeds at each point on a stroke.
    param speed_threshold_1 : a percentage (between 0 and 1). The threshold determines the
        maximum percentage of the average pen speed allowed for a point to be considered a
        segmentation point.

    return : a list of all segmentation points
    """

    # returning list of indices for now
    avg_speed = sum(smoothed_pen_speeds) / len(smoothed_pen_speeds)
    threshold = avg_speed * speed_threshold_1

    indices = []
    for i in range(len(smoothed_pen_speeds)):
        if smoothed_pen_speeds[i] < threshold:
            indices.append(i)

    return indices

def compute_corners_using_curvature_and_speed(stroke, smoothed_pen_speeds, curvatures,
    curvature_threshold=CURVATURE_THRESHOLD, speed_threshold_2=SPEED_THRESHOLD_2):
    """
    param stroke : a Stroke object with N x,y,t data points
    param smoothed_pen_speeds : an array of the smoothed pen speeds at each point on a stroke.
    param curvatures : an array of curvatures
    param curvature_threshold : in degress per pixel. The minimum threshold for the curvature of
        a point for the point to be considered a segmentation point.
    param speed_threshold_2 : a percentage (between 0 and 1). The threshold determines the
        maximum percentage of the average pen speed allowed for a point to be considered a
        segmentation point.


    return : a list of all segmentation points
    """
    assert len(smoothed_pen_speeds) == len(curvatures)
    avg_speed = sum(smoothed_pen_speeds) / len(smoothed_pen_speeds)
    speed_threshold = avg_speed * speed_threshold_2

    indices = []
    for i in range(len(smoothed_pen_speeds)):
        if smoothed_pen_speeds[i] < speed_threshold and abs(curvatures[i]) > curvature_threshold:
            indices.append(i)

    return indices

def combine_corners(stroke, cumulative_arc_lengths, corners_using_speed_alone,
    corners_using_curvature_and_speed, minimum_distance_between_corners=MINIMUM_DISTANCE_BETWEEN_CORNERS):
    """
    param stroke : a Stroke object with N x,y,t data points
    param cumulative_arc_lengths : an array of the cumulative arc lengths of the stroke
    param corners_using_speed_alone : a list of all segmentation points found using speed
    param corners_using_curvature_and_speed : a list of all segmentation points found using
        curvature and speed
    param minimum_distance_between_corners : minimum distance allowed between two segmentation
        points.

    return : a list of all segmentation points, with nearly coincident points removed. The list
    should be sorted from first to last segmentation point along the stroke.
    """
    n = len(stroke.x)
    def dist_between_points(a, b):
        return math.hypot(stroke.x[a] - stroke.x[b], stroke.y[a] - stroke.y[b])

    all_candidates = set(corners_using_speed_alone + corners_using_curvature_and_speed)
    nodes = []
    nodes.append(set([0]))
    nodes.append(set([n - 1]))
    for cand in sorted(list(all_candidates)):
        assigned = False
        for node_set in nodes:
            belongs = any(dist_between_points(cand, x) < minimum_distance_between_corners for x in node_set)
            if belongs:
                node_set.add(cand)
                assigned = True
                break
        if not assigned:
            nodes.append(set([cand]))
    def get_correct_node(node_set):
        if 0 in node_set:
            return 0
        elif n - 1 in node_set:
            return n - 1
        else:
            return sorted(list(node_set))[len(node_set) // 2]
    keep = [get_correct_node(node_set) for node_set in nodes]
    return sorted(list(keep))

def compute_linear_error(stroke, start_point, end_point):
    """
    param stroke : a Stroke object with N x,y,t data points
    param start_point : a segmentation point, representing the index into the stroke
        where the segment begins
    param end_point : a segmentation point, respresenting the index into the stroke
        where the segment ends

    return : the residual error of the linear fit
    """
    if start_point == end_point:
        return 0

    xs = stroke.x[start_point : end_point + 1]
    ys = stroke.y[start_point : end_point + 1]

    m, b = np.polyfit(xs, ys, 1)

    residuals = []
    for x, y in zip(xs, ys):
        residuals.append(abs(y - (m * x + b)))

    return sum(residuals) / len(residuals)

def compute_circular_error(stroke, start_point, end_point):
    """
    param stroke : a Stroke object with N x,y,t data points
    param start_point : a segmentation point, representing the index into the stroke
        where the segment begins
    param end_point : a segmentation point, respresenting the index into the stroke
        where the segment ends

    return : the residual error of the circle/curve fit
    """
    xs = stroke.x[start_point : end_point + 1]
    ys = stroke.y[start_point : end_point + 1]
    cx, cy, radius = circle_fit(xs, ys)

    residuals = []
    for x, y in zip(xs, ys):
        residuals.append(abs(math.hypot(cx - x, cy - y) - radius))

    return sum(residuals) / len(residuals)

def compute_subtended_angle(stroke, start_point, end_point):
    """
    param stroke : a Stroke object with N x,y,t data points
    param start_point : a segmentation point, representing the index into the stroke
        where the segment begins
    param end_point : a segmentation point, respresenting the index into the stroke
        where the segment ends

    return : the angle subtended by the arc of the circle fit to the segment
    """
    xs = stroke.x[start_point : end_point + 1]
    ys = stroke.y[start_point : end_point + 1]
    cx, cy, radius = circle_fit(xs, ys)

    r2 = radius * radius
    def get_point_on_circle(x, y, cx, cy, r):
        d = math.hypot(x - cx, y - cy)
        ratio = r / d
        return (ratio * (x - cx) + cx, ratio * (y - cy) + cy)

    p1 = get_point_on_circle(xs[0], ys[0], cx, cy, radius)
    p2 = get_point_on_circle(xs[-1], ys[-1], cx, cy, radius)
    c2 = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    init_angle = math.acos((2 * r2 - c2) / (2 * r2))

    circumference = 2 * math.pi * radius
    cumulative_arc_lengths = compute_cumulative_arc_lengths(stroke)
    approx_arc = cumulative_arc_lengths[end_point] - cumulative_arc_lengths[start_point]

    if approx_arc < circumference / 2:
        return init_angle
    else:
        return 2 * math.pi - init_angle

def choose_segment_type(stroke, linear_error, circular_error, subtended_angle, minimum_arc_angle=MINIMUM_ARC_ANGLE):
    """
    param stroke : a Stroke object with N x,y,t data points
    param linear_error : residual error of the linear fit of the segment
    param circular_error : residual error of the circular fit of the segment
    param subtended_angle : angle subtended by the arc of the circle
    param minimum_arc_angle : minimum angle necessary for classification as a curve

    return : 0 if the segment should be a line; 1 if the segment should be a curve
    """
    if linear_error < circular_error:
        return 0

    # only fit arc if stroke represents at least part of the circle
    if math.degrees(subtended_angle) > minimum_arc_angle:
        return 1
    else:
        return 0

def merge(stroke, segpoints, segtypes):
    """
    TODO (optional): define your function signature. You may change the function signature,
    but please name your function 'merge'. You may use helper functions.
    """
    final_segpoints = [segpoints[0]]
    final_segtypes = []
    i = 0
    while i < len(segtypes) - 1:
        # if consecutive ones are lines
        if segtypes[i] == segtypes[i + 1]:
            compute_error = compute_linear_error if segtypes[i] == 0 else compute_circular_error
            seg_1_err = compute_error(stroke, segpoints[i], segpoints[i+1])
            seg_2_err = compute_error(stroke, segpoints[i+1], segpoints[i+2])
            seg_all_err = compute_error(stroke, segpoints[i], segpoints[i+2])
            if seg_all_err < MERGE_FIT_ERROR_THRESHOLD * (seg_1_err + seg_2_err):
                i += 1
                continue
        final_segpoints.append(segpoints[i+1])
        final_segtypes.append(segtypes[i])
        i += 1
    final_segpoints.append(segpoints[-1])
    final_segtypes.append(segtypes[-1])
    assert len(final_segpoints) == len(final_segtypes) + 1
    return final_segpoints, final_segtypes

# NOTE: do not modify except for optional extra credit portion
def segment_stroke(stroke):
    """
    param stroke : a Stroke object with N x,y,t data points

    return :
        segpoints : an array of length M containing the segmentation points
            of the stroke. Each element in the array is an index into the stroke.
        segtypes : an array of length M-1 containing 0's (indicating a line)
            and 1's (indicating an arc) that describe the type of segment between
            segmentation points. Element i defines the type of segment between
            segmentation points i and i+1.
    """

    segpoints, segtypes = [], []

    # PART 1
    cumulative_arc_lengths = compute_cumulative_arc_lengths(stroke)

    # PART 2
    smoothed_pen_speeds = compute_smoothed_pen_speeds(stroke, cumulative_arc_lengths)

    # PART 3
    tangents = compute_tangents(stroke)

    # PART 4
    angles = compute_angles(stroke, tangents)
    plot_angles(stroke, angles)
    corrected_angles = correct_angles(stroke, angles)
    plot_angles(stroke, corrected_angles)
    curvatures = compute_curvatures(stroke, cumulative_arc_lengths, corrected_angles)

    # PART 5
    corners_using_speed_alone = compute_corners_using_speed_alone(stroke, smoothed_pen_speeds)
    corners_using_curvature_and_speed = compute_corners_using_curvature_and_speed(stroke, smoothed_pen_speeds, curvatures)

    # PART 6
    segpoints = combine_corners(stroke, cumulative_arc_lengths, corners_using_speed_alone, corners_using_curvature_and_speed)

    # PART 7
    for i in range(len(segpoints) - 1):
        start_point = segpoints[i]
        end_point = segpoints[i + 1]
        linear_error = compute_linear_error(stroke, start_point, end_point)
        circular_error = compute_circular_error(stroke, start_point, end_point)
        subtended_angle = compute_subtended_angle(stroke, start_point, end_point)
        segment_type = choose_segment_type(stroke, linear_error, circular_error, subtended_angle)
        segtypes.append(segment_type)

    # OPTIONAL: PART 10
    segpoints, segtypes = merge(stroke, segpoints, segtypes)

    return segpoints, segtypes
