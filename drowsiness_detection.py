from numpy.linalg import norm
from imutils import face_utils
import dlib
import cv2

cap = cv2.VideoCapture(0)

ear_thresh = 0.15
count_ear = 0
count_ear_thresh = 20
curr_state = 0
ave_ear = 0

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
left_start, left_end = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
right_start, right_end = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

def eye_aspect_ratio(eye):
  A = norm(eye[0] - eye[3])
  B = norm(eye[1] - eye[5])
  C = norm(eye[2] - eye[4])
  return (B + C) / (2.0 * A)

while True:
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  rects = detector(gray, 0)
  
  if len(rects) >= 1 :
    rec = rects[0]
    shape = predictor(gray, rec)
    shape = face_utils.shape_to_np(shape)

    left_eye = shape[left_start:left_end]
    ear_left_eye = eye_aspect_ratio(left_eye)

    right_eye = shape[right_start:right_end]
    ear_right_eye = eye_aspect_ratio(right_eye)

    ave_ear = (ear_left_eye + ear_right_eye) / 2.0

    leftEyeHull = cv2.convexHull(left_eye)
    rightEyeHull = cv2.convexHull(right_eye)

    if ave_ear < 0.2:
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 0, 255), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 0, 255), 1)
        count_ear += 1
    else:
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
        count_ear = 0

  if count_ear > 30:
      cv2.putText(frame, "SLEEP DETECTION !!!", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255),
                  lineType=cv2.LINE_AA)

  cv2.putText(frame, "EAR: {:.2f}".format(ave_ear), (300, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
  cv2.imshow('sleep detection', frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()
