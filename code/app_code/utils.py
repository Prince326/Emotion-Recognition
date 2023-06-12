import cv2
import os as os



def gen():
    while True:
        import warnings
        warnings.filterwarnings("ignore")

        # Capture a frame from the webcam
        capture_images = cv2.VideoCapture(0)
        ret, frame = capture_images.read()

        # Check if image capture is enabled
        if capture_images :

            # Set the filename to include the current timestamp
            filename = os.path.join("captures", "image.jpg")

            # Save the frame to the specified directory
            cv2.imwrite(filename, frame)

            flag = 1

            #Convert the frame to JPEG format

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


