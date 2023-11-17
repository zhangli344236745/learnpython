import cv2
import cv2 as cv

img = cv.imread("boy.jpg")
print(img.shape)
print(img.size)
print(img.dtype)
cv.imshow("img",img)
gray_image = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
hsv_image = cv.cvtColor(img,cv2.COLOR_BGR2HSV)
cv.imshow("img_gray",gray_image)
cv.imshow("hsv_image",hsv_image)
cut_img = img[20:100,20:50]
print(cut_img.shape)
cv.imshow("cut",cut_img)
cv.waitKey(0)
cv.destroyAllWindows()