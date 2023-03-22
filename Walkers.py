# import the opencv library
import cv2

# Define a video capture object
cap = cv2.VideoCapture('PRO-106-ProjectTemplate-main/walking.avi')
body_cascade=cv2.CascadeClassifier('PRO-106-ProjectTemplate-main/haarcascade_fullbody.xml')
while(True):
    
    # Capture the video frame by frame
    ret, frame = cap.read() 

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    body= body_cascade.detectMultiScale(gray,1.2,3)
    #1.1= scale factor, this parameter sets the % amount to reduce the size of the detection window,possible range=1.1 - 1.9 more the no. more the accuracy
    #5= minNeighbours, how many facial features that need to be present to detect the face
        
    for (x,y,w,h) in body:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    
    # Display the resulting frame
    cv2.imshow("Walking", frame)
      
    # Quit Window by Spacebar Key
    if cv2.waitKey(25) == 32:
        break
  
# After the loop release the cap object
cap.release()

# Destroy all the windows
cv2.destroyAllWindows()