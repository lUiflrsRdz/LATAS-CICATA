
import cv2
import numpy as np
import json
import findsold

with open('data.json') as f:
  data = json.load(f)

#print(data)
#print(data["parametros"][0]["Hue Minimo"])

hMin = data["parametros"][0]["Hue Minimo"]
hMax = data["parametros"][0]["Hue Maximo"]
sMin = data["parametros"][0]["Saturation Minimo"]
sMax = data["parametros"][0]["Saturation Maximo"]
vMin = data["parametros"][0]["Value Minimo"]
vMax = data["parametros"][0]["Value Maximo"]
kernelx = data["parametros"][0]["Kernel X"]
kernely = data["parametros"][0]["Kernel Y"]

for i in range(9): 

	  #Cargamos la imagen y la convertimos a HSV:
	  img = cv2.imread("latas/"+str(i)+".jpg")
	  img = cv2.resize(img, (640, 480))
	  Original = img
	  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	  #Creamos los arrays que definen el rango de colores:
	  color_bajos=np.array([hMin,sMin,vMin])
	  color_altos=np.array([hMax,sMax,vMax])
	 
	  
	  #Creamos el kernel:
	  kernel = np.ones((kernelx,kernely),np.uint8)
	 
	  #Detectamos los colores y eliminamos el ruido:
	  mask = cv2.inRange(hsv, color_bajos, color_altos)
	  mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
	  mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	  kernel = np.ones((7,7),np.uint8)
	  mask = cv2.dilate(mask,kernel,iterations = 1)
	  HSV = mask

	  contours, hierarchy = cv2.findContours(mask,1,2)
	  CountMax = 0
	  IdxMax = 0

	  for cnt in contours:
	    
	  	x,y,w,h = cv2.boundingRect(cnt)
	  	if w * h > CountMax:
	  		CountMax = w * h
	  		IdxMax = cnt

	  x,y,w,h = cv2.boundingRect(IdxMax)
	  img=img[y:y+h,x:x+w]
	  mask=mask[y:y+h,x:x+w]
	  cv2.rectangle(Original,(x,y),(x+w,y+h),(0,255,0),2)

	  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )
	  ret,BW = cv2.threshold(img,170,255,cv2.THRESH_BINARY)

	  #Mostramos los resultados y salimos:
	  cv2.imshow('Original',Original)
	  cv2.imshow('HSV',HSV)
	  cv2.imshow('Gray',img)
	  cv2.imshow('Mascara',BW)

	  cv2.waitKey(0) # waits until a key is pressed
	  cv2.destroyAllWindows()
