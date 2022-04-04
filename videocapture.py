import os
import cv2
import uuid

# Use uuid library to generate unique image names in Anchor
os.path.join('D:\Selva\Capstone Projects\5 DL & MLE\FaceRecognition & DrowsinessDetection\Anchor', '{}.jpg'.format(uuid.uuid1()))

# Establish a connection to the webcam
cap = cv2.VideoCapture(0)
print("[INFO] Press q to exit webcam")
while True: 
    ret, frame = cap.read()
   
    # Cut down frame to 250x250px
    frame = frame[120:120+250,200:200+250, :]

    # Collect anchors 
    if cv2.waitKey(1) & 0XFF == ord('a'):
        # Create the unique file path 
        imgname = os.path.join('D:/Selva/Capstone Projects/5 DL & MLE/FaceRecognition & DrowsinessDetection/Anchor', '{}.jpg'.format(uuid.uuid1()))
        # Write out anchor image
        cv2.imwrite(imgname, frame)
    
    # Collect positives
    if cv2.waitKey(1) & 0XFF == ord('p'):
        # Create the unique file path 
        imgname = os.path.join('D:/Selva/Capstone Projects/5 DL & MLE/FaceRecognition & DrowsinessDetection/Positive', '{}.jpg'.format(uuid.uuid1()))
        # Write out positive image
        cv2.imwrite(imgname, frame)
    
    # Show image back to screen
    cv2.imshow('Image Collection', frame)
    
    # Breaking gracefully
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
        
# Release the webcam
cap.release()
# Close the image show frame
cv2.destroyAllWindows()