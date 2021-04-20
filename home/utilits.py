
from cv2 import cv2
from PIL import Image

face_cascade = cv2.CascadeClassifier('D:\\HTML\\django\\facedectection\\home\\haarcascade_frontalface_default.xml') # We load the cascade for the face.

#input size of image to the model is(48,48,1)
def detect(gray, frame):# We apply the detectMultiScale method from the face cascade to locate one or several faces in the image.
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 5)# We paint a rectangle around the face.    
        return frame

def open_img(request):
    video_capture = cv2.VideoCapture(0)# We turn the webcam on.
    while True:
        _, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        canvas = detect(gray, frame)
        cv2.imshow('Video', canvas)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release() # We turn the webcam off.
    cv2.destroyAllWindows() # We destroy all the windows inside which the images were displayed.

def upload_img(image_path):
    #print(image_path)
    img=cv2.imread(image_path)
    #print(img)
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 5)
    #img=img=cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    img_pil=Image.fromarray(img)
    
    return img_pil

