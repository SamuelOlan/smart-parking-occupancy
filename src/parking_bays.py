import cv2
import numpy as np


def find_bay(px, py, bays):
    """Return the name of the bay containing (px, py), or None."""
    for bay_name, points in bays.items():
        polygon = np.array(points, dtype=np.int32)

        inside = cv2.pointPolygonTest(
            polygon,
            (float(px), float(py)),
            False
        )

        if inside >= 0:
            return bay_name

    return None
