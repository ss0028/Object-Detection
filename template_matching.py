#Created by Shikha Singh

#importing the  required libraries
import cv2,numpy as np

#loading the image from which an object is to be detected
img = cv2.imread('C:/Users/pluto/folder_img/food.jpg')
#displaying the original image
cv2.imshow('where is gulab-jamun??',img)
#through waitKey function, the image window exits on any button clicked by the user
cv2.waitKey(0)

#grayscaling the image
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#giving a sample to the machine of object to be found
template = cv2.imread('C:/Users/pluto/folder_img/object.jpg')
#dispalying the object to be found
cv2.imshow("object to be detected",template)
#converting the object to grayscale color space for further processing 
template_gray = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
cv2.waitKey(0)

#using matchTemplate function in cv2 to locate the object in the image using template matching technique
#cv2.TM_CCOEFF is a matching method which returns an array, here named  result
#result stores the result of template matching procedure
result = cv2.matchTemplate(gray,template_gray,cv2.TM_CCOEFF)

#cxv2.minMaxLoc gives the coordinates of the bounding box in which object was found
min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)
top_left = max_loc
bottom_right = (top_left[0]+235,top_left[1]+180)

#creating a rectangle around the box, to highlight the object
cv2.rectangle(img,top_left,bottom_right,(0,0,255),5)

cv2.imshow('gulabjamun found',img)
cv2.waitKey(0)

cv2.destroyAllWindows()
