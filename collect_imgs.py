import os
import cv2

DATA_DIR = 'C:/Users/risha/Documents/PROJECTS/Sign detection using Python/data'

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3
dataset_size = 100

cap = cv2.VideoCapture(0)  # Ensure the correct camera index (try 0 if 2 doesn't work)
for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print('Collecting data for class {}'.format(j))

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame from camera.")
            break
        
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame from camera.")
            break

        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        
        # Save the image only if the frame is valid
        img_path = os.path.join(class_dir, '{}.jpg'.format(counter))
        cv2.imwrite(img_path, frame)
        # print(f"Saved image: {img_path}")  #to show where the images are saved
        

        counter += 1

cap.release()
cv2.destroyAllWindows()
