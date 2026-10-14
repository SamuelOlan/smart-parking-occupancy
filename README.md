# Smart Parking Occupancy

This project uses YOLO and OpenCV to estimate parking-bay occupancy from a video. The notebook contains the original workflow. The Python modules provide a small local pipeline that detects vehicles, checks whether they fall inside configured bays, and writes an annotated video.

## Project layout

```text
run_video.py                 Local video runner
requirements.txt             Python dependencies
.gitignore                   Local files excluded from Git
LICENSE                      Project license
notebooks/                   Original notebook workflow
src/detector.py              YOLO model wrapper
src/parking_bays.py          Point-in-bay geometry
src/occupancy.py             Detection-to-occupancy logic
src/video_processor.py        Frame processing and video output
tests/test_occupancy.py      Occupancy unit tests
data/                        Local input videos (not tracked)
outputs/                     Generated files (not tracked)
```

## Set up

Use Python 3.10 or newer in a virtual environment, then install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run on a local video

Put the camera video at `data/parking1.mp4`, then run:

```bash
python run_video.py
```

The annotated video is written to `outputs/smart_parking_output.mp4`. To use a different input file, change `INPUT_VIDEO` in `run_video.py`.

The bay coordinates in `run_video.py` match the camera view used in the notebook. Recalibrate them for a different camera or video. The YOLO weights are loaded by Ultralytics when `VehicleDetector` is created.

## Run the tests

```bash
python -m pytest
```

## Current limits

- The local pipeline writes an annotated video; CSV export and detection-box labels are not implemented there yet.
- Occupancy depends on the YOLO detections and the chosen reference point near the bottom of each detection box.
- The supplied bay coordinates only apply to the original camera view.
- The notebook still contains its own end-to-end implementation and is useful for comparing behavior.
