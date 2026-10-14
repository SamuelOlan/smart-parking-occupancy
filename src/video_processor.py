"""Read a video, estimate occupancy, and write an annotated copy."""

import cv2
import numpy as np

from src.occupancy import get_occupied_bays
from src.parking_bays import find_bay


def process_video(video_path, output_path, detector, bays):
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        raise RuntimeError(f"Could not open video: {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    if fps <= 0 or frame_width <= 0 or frame_height <= 0:
        cap.release()
        raise RuntimeError("Video metadata is invalid.")

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(
        str(output_path), fourcc, fps, (frame_width, frame_height)
    )
    if not writer.isOpened():
        cap.release()
        writer.release()
        raise RuntimeError(f"Could not create output video: {output_path}")

    frame_index = 0
    try:
        while True:
            success, frame = cap.read()
            if not success:
                break

            result = detector.detect(frame)
            boxes = [box.xyxy[0].tolist() for box in result.boxes]
            occupied = get_occupied_bays(boxes, bays, find_bay)

            for bay_name, points in bays.items():
                polygon = np.array(points, dtype=np.int32)
                color = (0, 0, 255) if bay_name in occupied else (0, 255, 0)
                cv2.polylines(
                    frame, [polygon], isClosed=True, color=color, thickness=2
                )

            writer.write(frame)
            frame_index += 1

            if frame_index % 50 == 0:
                print(f"Processed {frame_index} frames")
    finally:
        cap.release()
        writer.release()
