"""Tests for mapping vehicle detections to parking bays."""

from src.occupancy import get_occupied_bays
from src.parking_bays import find_bay


SAMPLE_BAYS = {
    "bay1": [[0, 0], [100, 0], [100, 100], [0, 100]],
}


def test_detection_reference_point_inside_bay_marks_it_occupied():
    detections = [(20, 20, 60, 80)]

    result = get_occupied_bays(detections, SAMPLE_BAYS, find_bay)

    assert result == {"bay1"}


def test_detection_outside_all_bays_marks_nothing_occupied():
    detections = [(120, 20, 160, 80)]

    result = get_occupied_bays(detections, SAMPLE_BAYS, find_bay)

    assert result == set()


def test_multiple_detections_in_same_bay_count_bay_once():
    detections = [(20, 20, 60, 80), (30, 10, 70, 90)]

    result = get_occupied_bays(detections, SAMPLE_BAYS, find_bay)

    assert result == {"bay1"}
