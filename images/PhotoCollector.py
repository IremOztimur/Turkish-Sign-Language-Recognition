import os
import time
import uuid
import cv2

image_path = "collectedimages"

labels = ['merhaba', 'gunaydin', 'turk', 'lutfen']
number_imgs = 50

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Failed to open the camera.")
    exit()

time.sleep(2)

for label in labels:
    directory = os.path.join(image_path, label)
    os.makedirs(directory, exist_ok=True)

    num_images_for_label = number_imgs
    print("Collecting images for {}".format(label))

    while True:
        ret, frame = cap.read()

        # Check if the frame is valid
        if not ret:
            print("Error: Failed to capture frame.")
            break

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('p'):
            imgname = os.path.join(image_path, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
            print("written to {}".format(imgname))

            write_status = cv2.imwrite(imgname, frame)

            num_images_for_label -= 1

            if num_images_for_label != 0 and write_status:
                print('Saved, {} left for {}'.format(num_images_for_label, label))
        elif (cv2.waitKey(1) & 0xFF == ord('q')) or num_images_for_label == 0:
            break


cap.release()
cv2.destroyAllWindows()
