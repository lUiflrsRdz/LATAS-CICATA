import cv2
import numpy as np
import json

def Find_Sold(mask, img):
	#mask = cv2.bitwise_not(mask)
	contours, hierarchy = cv2.findContours(mask,1,2)
	#print(contours)
	h, w, c = img.shape
	#roi=mask[Contorno[1]:Contorno[1]+Contorno[3],Contorno[0]:Contorno[0]+Contorno[2]]

	idx =0 
	ContornoMayor= 0
	Contorno = [0, 0, 0, 0]
	for cnt in contours:
	    idx += 1
	    x,y,w,h = cv2.boundingRect(cnt)
	    #print(x,y,w,h)
	    contor = w+h	
	    if contor > ContornoMayor:
	    	if w/h > 0.5 and w/h < 1.5:
	    		Contorno[0] = x
	    		Contorno[1] = y
	    		Contorno[2] = w
	    		Contorno[3] = h
	    #roi=img[y:y+h,x:x+w,:]
	#print(Contorno)
	#cv2.rectangle(mask,(x,y),(x+w,y+h),(0,255,0),2)
	#cv2.imwrite("segmentacion/sold"+str(area)+str(idx) + '.jpg', img)
	cv2.drawContours(mask, contours, -1, (0, 255, 0), 3)
	roi=mask[Contorno[1]:Contorno[1]+Contorno[3],Contorno[0]:Contorno[0]+Contorno[2]]
	#image = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
	#ret,thresh1 = cv2.threshold(image,200,255,cv2.THRESH_BINARY)
	#

	return roi, Contorno


def Find_Sold1(ROIAct):

	#print(AllROIs[0])

	img = cv2.imread("ImageToCalibrate.jpg")

	dtype_after = type(ROIAct)
	arr = np.array(ROIAct)

	#print(arr)

	#print(arr[0,0])
	#print(arr[0,1])
	#print(arr[0,2])
	#print(arr[0,3])
	#print(arr[1,0])
	#print(arr[1,1])
	#print(arr[1,2])
	#print(arr[1,3])
	#print(arr[2,0])
	#print(arr[2,1])
	#print(arr[2,2])
	#print(arr[2,3])
  
	#img = cv2.resize(img, (720, 480))
	roi1=img[arr[0,1]:arr[0,1]+arr[0,3],arr[0,0]:arr[0,0]+arr[0,2],:]
	roi2=img[arr[1,1]:arr[1,1]+arr[1,3],arr[1,0]:arr[1,0]+arr[1,2],:]
	roi3=img[arr[2,1]:arr[2,1]+arr[2,3],arr[2,0]:arr[2,0]+arr[2,2],:]

	image1 = cv2.cvtColor(roi1, cv2.COLOR_BGR2GRAY )
	image2 = cv2.cvtColor(roi2, cv2.COLOR_BGR2GRAY )
	image3 = cv2.cvtColor(roi3, cv2.COLOR_BGR2GRAY )

	ret1,thresh1 = cv2.threshold(image1,170,255,cv2.THRESH_BINARY)
	ret2,thresh2 = cv2.threshold(image2,170,255,cv2.THRESH_BINARY)
	ret3,thresh3 = cv2.threshold(image3,170,255,cv2.THRESH_BINARY)

	mask1 = Find_Sold(thresh1, roi1, 1)
	mask2 = Find_Sold(thresh2, roi2, 2)
	mask3 = Find_Sold(thresh3, roi3, 3)

	cv2.imwrite("segmentacion/"+str(1)+".jpg",image1)
	cv2.imwrite("segmentacion/"+str(2)+".jpg",image2)
	cv2.imwrite("segmentacion/"+str(3)+".jpg",image3)

	cv2.imwrite("segmentacion/sold"+str(1)+".jpg",mask1)
	cv2.imwrite("segmentacion/sold"+str(2)+".jpg",mask2)
	cv2.imwrite("segmentacion/sold"+str(3)+".jpg",mask3)

	return 0
