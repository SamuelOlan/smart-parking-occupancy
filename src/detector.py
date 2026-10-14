"""YOLO vehicle detector used by the video pipeline."""

from ultralytics import YOLO


class VehicleDetector:
    def __init__(self, model_path: str = "yolov8n.pt") -> None:
        self.model = YOLO(model_path)

    def detect(self, frame):
        """Return YOLO's result for one OpenCV frame."""
        results = self.model.predict(
            source=frame,
            classes=[2, 3, 5, 7],
            conf=0.25,
            imgsz=960,
            verbose=False,
        )
        return results[0]
