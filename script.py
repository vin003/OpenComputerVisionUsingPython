import cv2
im1=cv2.imread("galaxy.jpg",0)
im2=cv2.imread("kangaroos.jpg",0)
im3=cv2.imread("Lighthouse.jpg",0)
im4=cv2.imread("moon.jpg",0)


new_im1=cv2.resize(im1,(100,100))
cv2.imwrite("galaxy_1.jpg",new_im1)
new_im2=cv2.resize(im2,(100,100))
cv2.imwrite("kangaros_1.jpg",new_im2)
new_im3=cv2.resize(im3,(100,100))
cv2.imwrite("Lighthouse_1.jpg",new_im3)
new_im4=cv2.resize(im4,(100,100))
cv2.imwrite("moon_1.jpg",new_im4)