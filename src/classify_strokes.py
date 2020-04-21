import math
from stroke_segmentation import segment_stroke

def normalize_segpoints(stroke):
    """
    param stroke : a Stroke object with N x,y,t data points

    return :
        (template_x, template_y): a tuple of arrays representing the normalized X
        and Y coordinates, ordered by time, of the points to be
        used in the MHD calculation to compare against the given templates

        Coordinates are normalized so that points span between 0 and 1

        Relevant points would be the full set of stroke segment endpoints
        and the curve segment midpoints

    """
    #NORMALIZE THE STROKE POINTS

    #GET THE SET OF POINTS TO BE USED IN THE MHD CALCULATION

    template_x = []
    template_y = []

    segpoints, segtypes = segment_stroke(stroke)
    assert len(segpoints) == len(segtypes) + 1

    for i in range(len(segtypes)):
        point = segpoints[i]
        template_x.append(stroke.x[point])
        template_y.append(stroke.y[point])
        if segtypes[i] == 1:
            midpoint = (segpoints[i] + segpoints[i + 1]) // 2
            template_x.append(stroke.x[midpoint])
            template_y.append(stroke.y[midpoint])
    last_point = segpoints[-1]
    template_x.append(stroke.x[last_point])
    template_y.append(stroke.y[last_point])

    num_arcs = sum([t for t in segtypes if t == 1])
    assert len(template_x) == len(segpoints) + num_arcs

    min_x, max_x = min(template_x), max(template_x)
    min_y, max_y = min(template_y), max(template_y)
    diff_x = max_x - min_x
    diff_y = max_y - min_y
    template_x = [(x - min_x) / diff_x for x in template_x]
    template_y = [(y - min_y) / diff_y for y in template_y]

    return template_x, template_y

def calculate_MHD(stroke, template):
    """
    param stroke : a Stroke object with N x,y,t data points
    param template : a Template object with x,y template points and name

    return :
        float representing the Modified Hausdorff Distance of the normalized segpoints
        and the template points,
        The formula for the Modified Hausdorf Distance can be found in the
        paper "An image-based, trainable symbol recognizer for
        hand-drawn sketches" by Kara and Stahovichb

    """
    def directed_mhd(Ax, Ay, Bx, By):
        assert len(Ax) == len(Ay)
        assert len(Bx) == len(By)
        min_dists = [
            min([math.hypot(ax - bx, ay - by) for bx, by in zip(Bx, By)])
            for ax, ay in zip(Ax, Ay)]
        return (1 / len(Ax) * sum(min_dists))

    normalized_x, normalized_y = normalize_segpoints(stroke)

    return max(
        directed_mhd(normalized_x, normalized_y, template.x, template.y),
        directed_mhd(template.x, template.y, normalized_x, normalized_y))

def calculate_MHD_alt(normalized_x, normalized_y, template):
    """
    Like calculate_MHD but don't calculate normalized strokes each time
    """
    def directed_mhd(Ax, Ay, Bx, By):
        assert len(Ax) == len(Ay)
        assert len(Bx) == len(By)
        min_dists = [
            min([math.hypot(ax - bx, ay - by) for bx, by in zip(Bx, By)])
            for ax, ay in zip(Ax, Ay)]
        return (1 / len(Ax) * sum(min_dists))

    return max(
        directed_mhd(normalized_x, normalized_y, template.x, template.y),
        directed_mhd(template.x, template.y, normalized_x, normalized_y))

def classify_stroke(stroke, templates):
    """
    param stroke : a Stroke object with N x,y,t data points
    param templates: a list of Template objects, each with name, x, y
                     Each template represents a different symbol.

    return :
        string representing the name of the best matched Template of a stroke
    """
    normalized_x, normalized_y = normalize_segpoints(stroke)
    all_mhds = [(template.name, calculate_MHD_alt(normalized_x, normalized_y, template)) for template in templates]
    best = min(all_mhds, key=lambda x: x[1])[0]

    return best
