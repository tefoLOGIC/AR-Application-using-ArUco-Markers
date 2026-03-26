import cv2 as cv
from cv2 import aruco
import numpy as np
import os


def image_augmentation(frame, src_image, dst_points):
    if src_image is None:
        print("Source image is None")
        return

    src_h, src_w = src_image.shape[:2]
    frame_h, frame_w = frame.shape[:2]
    mask = np.zeros((frame_h, frame_w), dtype=np.uint8)
    src_points = np.array([[0, 0], [src_w, 0], [src_w, src_h], [0, src_h]], dtype=np.float32)
    dst_points = np.array(dst_points, dtype=np.float32)

    H, _ = cv.findHomography(src_points, dst_points)
    warp_image = cv.warpPerspective(src_image, H, (frame_w, frame_h))

    cv.fillConvexPoly(mask, np.int32(dst_points), 255)
    mask_inv = cv.bitwise_not(mask)

    frame_bg = cv.bitwise_and(frame, frame, mask=mask_inv)
    warp_fg = cv.bitwise_and(warp_image, warp_image, mask=mask)

    augmented_frame = cv.add(frame_bg, warp_fg)
    np.copyto(frame, augmented_frame)


def read_images(dir_path):
    img_list = []
    files = os.listdir(dir_path)
    for file in files:
        img_path = os.path.join(dir_path, file)
        image = cv.imread(img_path)
        if image is not None:
            img_list.append(image)
    return img_list


marker_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
param_markers = aruco.DetectorParameters()

images_list = read_images("../images/augmentation")

if not images_list:
    print("No images loaded for augmentation.")
    exit()

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read from the camera.")
            break

        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        marker_corners, marker_IDs, _ = aruco.detectMarkers(gray_frame, marker_dict, parameters=param_markers)

        if marker_corners:
            for ids, corners in zip(marker_IDs, marker_corners):
                corners = corners.reshape(4, 2).astype(int)
                marker_id = ids[0]
                if marker_id < len(images_list):
                    image_augmentation(frame, images_list[marker_id], corners)
                else:
                    print(f"Marker ID {marker_id} is out of range. Using the first image for augmentation.")
                    image_augmentation(frame, images_list[0], corners)

        cv.imshow("frame", frame)
        key = cv.waitKey(1)
        if key == ord("q"):
            break

except KeyboardInterrupt:
    print("Interrupted by user.")

finally:
    cap.release()
    cv.destroyAllWindows()
