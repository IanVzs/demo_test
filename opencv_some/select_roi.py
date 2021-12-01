
import cv2

img_battle = cv2.cvtColor(cv2.imread("axie_some/images/20211025-160926.png"), cv2.COLOR_BGR2RGB)

cv2.waitKey()
r = cv2.selectROI("input", img_battle, False)

