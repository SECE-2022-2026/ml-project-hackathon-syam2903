import cv2
from ar_overlay import AROverlay

def main():
    # Create an AROverlay object with the model path and 3D object path
    ar_overlay = AROverlay("yolov8n.pt", "cube.obj")
    
    # Open webcam (change 0 to the path of your video file if needed)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return
    
    while True:
        ret, frame = cap.read()  # Capture frame by frame

        if not ret:
            print("Error: Failed to capture frame.")
            break
        
        # Set the frame for AR overlay
        ar_overlay.set_frame(frame)
        
        # Overlay 3D object on the frame
        ar_overlay.overlay_3d_on_frame()

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()  # Release the video capture object
    cv2.destroyAllWindows()  # Close all OpenCV windows

if __name__ == "__main__":
    main()
