# pip install opencv-contrib-python
# pip install matplotlib
# pip install cvlib

import cv2
#
import matplotlib.pyplot as plt
#
# from cvlib import detect_common_objects
#
# from cvlib.object_detection import draw_bbox

import cvlib as cv
from cvlib.object_detection import draw_bbox
# img = cv2.imread("cars.jpeg")
# img = cv2.imread("fruit.jpeg")
video = cv2.VideoCapture(1)

end_points = {
    "person": 0.9762513041496277,
    "orange": 0.9320018887519836,
    "apple": 0.5922269225120544,
    "book": 0.5326956510543823
}

while True:
    ret, frame = video.read()
    bbox, label, conf = cv.detect_common_objects(frame)

    output_image = draw_bbox(frame, bbox, label, conf)

    cv2.imshow("Detection", output_image)

    labels = []
    for item in label:
        labels.append(item)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

for label in labels:
    print(label)
    # i = 0
    # i += 1
    # if i == 1:
    #     print(f"I found a {label}, and ")
    # else:
    #     print(f"a {label}")


# print(output_image)

# bbox, label, conf = detect_common_objects(img)
#
# output_image = draw_bbox(img, bbox, label, conf)
#
# plt.imshow(output_image)
#
# plt.show()

# print(f"Number of cars: {label.count}")