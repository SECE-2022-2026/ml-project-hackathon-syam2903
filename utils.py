import numpy as np
import cv2

def perspective_transform(frame, obj_points, frame_points):
    """
    Apply perspective transformation to place the 3D model correctly in the camera frame.
    """
    M = cv2.getPerspectiveTransform(np.float32(obj_points), np.float32(frame_points))
    result = cv2.warpPerspective(frame, M, (frame.shape[1], frame.shape[0]))
    return result
