import cv2
from PIL import Image
import math

def random_ellipse(self, image):
        h, w = image.shape[:2]
        center_x = random.randint(0, w - 1)
        center_y = random.randint(0, h - 1)

        axis_x = random.randint(0, min(w, h) // 2 - 1)
        axis_y = random.randint(0, min(w, h) // 2 - 1)

        angle = random.randint(0, 360)
        angles = [random.randint(0, 360), random.randint(0, 360)]
        angle_start = min(angles)
        angle_end = max(angles)
        color = random.randint(0, self._max_color)

        return cv2.ellipse(image, (center_x, center_y), (axis_x, axis_y), angle, angle_start,
                           angle_end, color, cv2.FILLED)


image = cv2.imread('D:/FOOTFALL_IMAGES/CMT_101_DG1 - MULTIPLE FOOTFALLS.jpeg')
random_ellipse(cv2.imread('D:/FOOTFALL_IMAGES/CMT_101_DG1 - MULTIPLE FOOTFALLS.jpeg'))
