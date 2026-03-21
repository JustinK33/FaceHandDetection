import cv2

cap = cv2.VideoCapture(0) # 0 means default webcam
success, frame = cap.read() # reads one frame

if not success:
    print("could not read from camera")
    cap.release()
    exit()

h, w = frame.shape[:2] # image height/width 
# frame is a numpy array and opencv usually stores that as (height, width, channels)
# thats why we use .shape[:2] we only want the first 2 values of the frame

# create:  cv2.FaceDetectorYN.create(model, config, input_size)
detector = cv2.FaceDetectorYN.create("face_detection_yunet_2023mar.onnx", "", (w, h))

last_box = None

while True:
    # tries to read one frame from cammera
    success, frame = cap.read()

    # success is whether it worked or not
    if not success:
        break

    h, w = frame.shape[:2]
    detector.setInputSize((w, h))
    _, faces = detector.detect(frame) # runs detection
    # faces is a array of numbers
    # the first 4 values being x, y, w, h
    # print(faces)

    if faces is not None:
        x, y, w, h = faces[0][:4].astype(int)
        last_box = (x, y, w, h)

    if last_box is not None:
        x, y, z, h = last_box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # frame is the actual frame
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) == 27: # 27 is the ESC key
        break

cap.release()
cv2.destroyAllWindows()