import cv2
import numpy as np
import json
import findsold

for i in range(27):

	img = cv2.imread("fotos lata/"+str(i+15)+".jpg")
	mask = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )	
	ret,mask = cv2.threshold(mask,200,255,cv2.THRESH_BINARY)

	#print("\nPulsa 'ESC' para salir\n")
	 
	 
	#while(1):
		#cv2.imshow('Original',img)
		#cv2.imshow('Mask',mask)
	#	k = cv2.waitKey(5) & 0xFF
	#	if k == 27:		
	#		break
	Contorno = []
	mask, Contorno = findsold.Find_Sold(mask,img)
	cv2.imwrite("segmentacion/lata"+str(i+15) + '.jpg', mask)
	#cv2.imshow('Mask',mask)
	#cv2.waitKey(0)
	
	print(Contorno)
	#print(idx)
	#cv2.destroyAllWindows()
#cv2.destroyAllWindows()
