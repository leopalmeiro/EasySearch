import cv2

img = cv2.imread("img/PaoyLeo.jpg", 1)

cv2.imshow("LeoAndPao", img)
cv2.waitKey(0)


cv2.destroyAllWindows()