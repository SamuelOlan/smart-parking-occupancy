"""Pure logic for mapping detections to occupied/vacant bays."""


def get_occupied_bays(detections, bays, find_bay_fn, bottom_point_raise=0.25):
    """Return a set of occupied bay names from detections and bay polygons.

    ``detections`` is an iterable of bounding boxes in (x1, y1, x2, y2)
    format. ``bottom_point_raise`` moves the reference point upward from the
    bottom of each box by that fraction of its height.
    """
    occupied_bays = set()

    for x1, y1, x2, y2 in detections:
        px = (x1 + x2) / 2
        py = y2 - bottom_point_raise * (y2 - y1)

        bay_name = find_bay_fn(px, py, bays)
        if bay_name is not None:
            occupied_bays.add(bay_name)

    return occupied_bays
