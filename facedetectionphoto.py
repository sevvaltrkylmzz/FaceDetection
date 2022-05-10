import matplotlib.pyplot as plt 
import cv2

 #reading image
img_cv= cv2.imread("./data/male_000281.jpg")
#converting into gray scale
gray=cv2.cvtColor(img_cv,cv2.COLOR_BGR2GRAY)
#apply haar cascade
haar=cv2.CascadeClassifier("./data/haarcascade_frontalface_default.xml")
 
faces=haar.detectMultiScale(gray,1.3,5)

for x,y,w,h in faces:
  cv2.rectangle(img_cv,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow("object_detect",img_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()

face_crop= img_cv[94:355,154:415]
cv2.imshow("cropped face",face_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("./data/male_01cropped.png",face_crop)
cv2.imwrite("./data/male_01.png",img_cv)