import numpy as np
import cv2

# Start a video capture
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while(True):

    # Capture the frames
    ret, frame = cap.read()

    # Try to come up with filters to better identify lines from the image!
    
    # Find the contours from the frame
    contours,hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)

    # Find the biggest contour (if detected)
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        
        try:
            M = cv2.moments(c)

            # Identify line from the countours
            # Here cx, cy indicates the center of the line (which will be the biggest contour on the image)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

            # Draw the contours on to the frame
            cv2.line(frame,(cx,0),(cx,720),(255,0,0),1)
            cv2.line(frame,(0,cy),(1280,cy),(255,0,0),1)
            cv2.drawContours(frame, contours, -1, (0,255,0), 1)

            # Try to set up conditions to decide how the robot should move based on the location of the line
            print("Go Straight!")

        except:
            print("I don't see the line")

    #Display the resulting frame
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()