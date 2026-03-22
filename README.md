# Real-Time Face & Hand Detection

A real-time computer vision app that detects faces and hand landmarks using OpenCV and MediaPipe, and overlays bounding boxes and skeletal hand connections directly from your webcam feed.

---

## Tech Stack

- Python
- OpenCV
- MediaPipe (Tasks API)
- NumPy

---

## Features (updating...)

- **Real-time webcam processing**
  - Captures live video stream using OpenCV
  - Processes frames continuously with low latency

- **Multi-face detection**
  - Uses OpenCV’s YuNet face detector
  - Detects and draws bounding boxes around multiple faces simultaneously

- **Hand landmark detection**
  - Uses MediaPipe Hand Landmarker (Tasks API)
  - Detects multiple hands in real time

- **Hand skeleton visualization**
  - Draws all 21 landmarks per hand
  - Connects landmarks using predefined hand connections to form a full skeletal structure

- **Asynchronous inference**
  - Uses MediaPipe’s `LIVE_STREAM` mode with async callbacks
  - Improves performance by decoupling detection from rendering

---

## 📚 What I Learned From This Project

- **Real-time video processing**
  Learned how to capture, process, and render frames efficiently using OpenCV while maintaining smooth performance.

- **Working with MediaPipe Tasks API**
  Understood how to use MediaPipe’s newer Tasks API, including async callbacks and handling streaming results.

- **Normalized → pixel coordinate conversion**
  Converted normalized landmark coordinates (0–1) into actual pixel positions for rendering on frames.

- **Handling asynchronous data**
  Managed async detection results using a shared global variable and synchronized it with the rendering loop.

- **Multi-object detection patterns**
  Learned to properly iterate over detection outputs (faces, hands) instead of only handling a single instance.

- **Debugging real-world CV issues**
  Fixed common issues like:
  - Only detecting one hand
  - Incorrect unpacking of detection outputs
  - Frame-to-frame artifact accumulation

- **Understanding detection vs tracking**
  Differentiated between:
  - Detecting objects each frame
  - Persisting objects across frames (tracking)

---

## Running the Project

### To run the project locally, follow these steps:

1. Clone the repo  
   `git clone <your-repo-url>`

2. Create a virtual environment  
   `python3 -m venv venv`

3. Activate the environment  
   `source venv/bin/activate`

4. Install dependencies  
   `pip install opencv-python mediapipe numpy`

5. Add required model files  
   - `face_detection_yunet_2023mar.onnx`
   - `hand_landmarker.task`

6. Run the script  
   `python main.py`

---

## Notes

- Press `ESC` to exit the webcam window
- Ensure your webcam is accessible (`cv2.VideoCapture(0)`)
- Performance depends on your machine (CPU-bound inference)

---

## Future Improvements

- Face tracking with IDs (instead of per-frame detection)
- Gesture recognition (e.g., counting fingers)
- FPS optimization and benchmarking
- UI overlays (labels, confidence scores)
- Integration into a web app (Flask / FastAPI)
