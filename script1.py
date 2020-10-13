import cv2
import glob

images=glob.glob("*_1.jpg")
print(images ,end= '')
for image in images:
    im1=cv2.imread("galaxy.jpg")
    new_im1=cv2.resize(im1,(100,100))
    cv2.imshow("hey",new_im1)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("Display"+image,new_im1)
