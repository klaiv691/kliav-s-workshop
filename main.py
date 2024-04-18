import cv2
import numpy as np
import serial
import time

# Load YOLO
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
layer_names = net.getUnconnectedOutLayersNames()

# Load COCO names
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Function to capture image, detect toy cars, count them, and send signal to Arduino
def capture_and_send_signal():
    # Initialize serial communication with Arduino
    arduino = serial.Serial('COM3', 9600)  # Replace 'COM3' with the actual port your Arduino is connected to

    # Open camera
    cap = cv2.VideoCapture(0)  # Use 0 for default camera, or change to the camera index if using an external camera

    while True:
        # Capture image from the camera
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to capture frame.")
            break

        # Get frame dimensions
        height, width = frame.shape[:2]

        # Detect toy cars in the frame
        detect_and_send_signal(frame, arduino, width, height)

        # Display the frame
        cv2.imshow("Frame", frame)

        # Wait for 7 seconds before capturing and detecting again
        time.sleep(10)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close serial connection
    cap.release()
    cv2.destroyAllWindows()
    arduino.close()

def detect_and_send_signal(frame, arduino, width, height):
    # Detect toy cars in the captured image
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(layer_names)

    num_cars = 0

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5 and classes[class_id] == "car":
                num_cars += 1

    # Print the number of cars detected
    print(f"Number of cars detected: {num_cars}")

    # Determine the message to send to the Arduino
    if num_cars < 3:
        message = "road1 go"
    else:
        message = "road2 go"

    # Print the message to be sent to the Arduino
    print(f"Sending message to Arduino: {message}")

    # Send the message to Arduino
    arduino.write(message.encode())

# Call the function to capture image, detect toy cars, count them, and send signal to Arduino
capture_and_send_signal()
