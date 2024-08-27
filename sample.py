import cv2

# Open the webcam
cap = cv2.VideoCapture(0)

from matplotlib import app
# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Read frames from the webcam
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame reading was successful
    if ret:
        # Display the resulting frame
        cv2.imshow('Webcam Feed', frame)

        # Press 'q' to break the loop and close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Error: Could not read frame.")
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
