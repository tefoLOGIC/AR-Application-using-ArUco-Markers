import cv2 as cv
from cv2 import aruco
import numpy as np

def image_augmentation(frame, src_image, dst_points):
    src_h, src_w = src_image.shape[:2]
    frame_h, frame_w = frame.shape[:2]

    mask = np.zeros((frame_h, frame_w), dtype=np.uint8)

    src_points = np.array([[0, 0], [src_w, 0], [src_w, src_h], [0, src_h]])

    H, _ = cv.findHomography(src_points, dst_points)

    warp_image = cv.warpPerspective(src_image, H, (frame_w, frame_h))

    cv.fillConvexPoly(mask, dst_points, 255)

    masked_frame = cv.bitwise_and(frame, frame, mask=cv.bitwise_not(mask))
    augmented_frame = cv.add(masked_frame, warp_image)

    frame[:, :] = augmented_frame

    return warp_image  # Return the warped image for further processing

def read_video(video_path):
    cap = cv.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return frames

param_markers = aruco.DetectorParameters()
marker_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)

video_frames = read_video(r"C:\Users\saima\Videos\6498520-uhd_2160_3840_25fps.mp4")  # Read video frames
video_frame_index = 0  # Index to track current video frame

cap = cv.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        marker_corners, marker_IDs, _ = aruco.detectMarkers(
            gray_frame, marker_dict, parameters=param_markers
        )

        if marker_corners:
            for ids, corners in zip(marker_IDs, marker_corners):
                corners = corners.reshape(4, 2).astype(int)

                if video_frame_index < len(video_frames):
                    warped_frame = image_augmentation(frame, video_frames[video_frame_index], corners)
                    video_frame_index += 1
                else:
                    video_frame_index = 0  # Reset video frame index to start from the beginning

        cv.imshow("frame", frame)

        key = cv.waitKey(1)
        if key == ord("q"):
            print("Quitting...")
            break

except KeyboardInterrupt:
    print("Interrupted by user")

finally:
    cap.release()
    cv.destroyAllWindows()
    print("Resources released, windows closed.")
