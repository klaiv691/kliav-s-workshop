import cv2

cascade_path = 'haarcascade_car.xml'

car_cascade = cv2.CascadeClassifier(cascade_path)

def detect_cars(image_path):

    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x, y, w, h) in cars:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Detected Cars', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = 'images (1).jfif'

detect_cars(image_path)
