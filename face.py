import cv2
import dlib

img = cv2.imread("doibong.jpg")

gray = cv2.cvtColor(src=img, code = cv2.COLOR_BGR2GRAY)

face_detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

faces = face_detector(gray) 
for face in faces:
    x1 = face.left()
    x2 = face.right()
    y1 = face.top()
    y2 = face.bottom()

    cv2.rectangle(img=img, pt1 = (x1,y1),pt2 =(x2,y2),color = (0,255,0), thickness= 2)
    face_features = predictor(image = gray, box = face)

    for i in range(0,68):
        x = face_features.part(i).x
        y = face_features.part(i).y
        cv2.circle(img = img, center= (x,y),radius=2, color=(0,0,255),thickness= 1)

print(len(faces))

cv2.imshow(winname = "Face", mat = img)

cv2.waitKey(delay = 0)

cv2.destroyAllWindows()