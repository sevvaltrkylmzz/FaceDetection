import cv2
haar = cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')
def face_detect(img):
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = haar.detectMultiScale(gray,1.3,5)
    
    for x,y,w,h in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        
    return img
cap = cv2.VideoCapture('./data/video.mp4')

while True:
    ret,frame = cap.read()
    if ret == False:
        break
        
    frame = face_detect(frame)
    cv2.imshow('object_detect',frame)
   
    if cv2.waitKey(20) == 27:
        break
cv2.destroyAllWindows()
cap.release()
