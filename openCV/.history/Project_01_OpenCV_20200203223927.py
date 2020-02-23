import cv2

img = cv2.imread("img/PaoyLeo.jpg", 1)

resized = cv2.resize(img, (600, 600))
cv2.imshow("LeoAndPao", img)
cv2.waitKey(0)


cv2.destroyAllWindows()