"""Run the parking occupancy pipeline on a local video."""

from pathlib import Path

from src.detector import VehicleDetector
from src.video_processor import process_video


PROJECT_DIR = Path(__file__).resolve().parent
INPUT_VIDEO = PROJECT_DIR / "data" / "parking1.mp4"
OUTPUT_VIDEO = PROJECT_DIR / "outputs" / "smart_parking_output.mp4"

# These polygons are calibrated for the camera view used in the notebook.
bays = {
    "bay1": [[85, 790], [180, 785], [148, 905], [38, 905]],
    "bay2": [[180, 785], [283, 780], [265, 905], [148, 905]],
    "bay3": [[283, 780], [395, 775], [395, 895], [265, 905]],
    "bay4": [[395, 775], [506, 765], [521, 885], [395, 895]],
    "bay5": [[506, 765], [620, 755], [652, 872], [521, 885]],
    "bay6": [[620, 755], [734, 745], [783, 857], [652, 872]],
    "bay7": [[734, 745], [843, 733], [907, 842], [783, 857]],
    "bay8": [[843, 733], [948, 720], [1023, 826], [907, 842]],
    "bay9": [[948, 720], [1045, 710], [1137, 810], [1023, 826]],
    "bay10": [[1045, 710], [1140, 700], [1237, 790], [1137, 810]],
    "bay11": [[1140, 700], [1226, 686], [1323, 769], [1237, 790]],
    "bay12": [[1226, 686], [1312, 672], [1409, 747], [1323, 769]],
}


def main():
    if not INPUT_VIDEO.is_file():
        raise FileNotFoundError(
            f"Input video not found: {INPUT_VIDEO}\n"
            "Place the camera video at data/parking1.mp4 or update INPUT_VIDEO."
        )

    detector = VehicleDetector()
    process_video(INPUT_VIDEO, OUTPUT_VIDEO, detector, bays)
    print(f"Annotated video saved to: {OUTPUT_VIDEO}")


if __name__ == "__main__":
    main()
