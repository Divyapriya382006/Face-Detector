import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)

while True:
    _,img=cap.read()
    #gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(img,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)
    cv2.putText(img,f"No of faces:{len(faces)}",(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),4)
    cv2.imshow('Image',img)

    if cv2.waitKey(1) and 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
        
