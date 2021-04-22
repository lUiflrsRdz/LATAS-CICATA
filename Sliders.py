# -*- coding: latin-1 -*-
"""
EJEMPLO 5 - Sliders
 
Este código detecta colores en una imagen estática. Los parámetros
(rango de colores, dimensión del kernel) pueden ajustarse mediante
sliders.
 
Escrito por Glare y Transductor
www.robologs.net
"""
import cv2
import numpy as np
import json
import findsold

data = {}
data['parametros'] = []

for i in range(9): 

	#Cargamos la imagen y la convertimos a HSV:
	img = cv2.imread("latas/"+str(i)+".jpg")
	img = cv2.resize(img, (640, 480))
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	 
	#Función auxiliar:
	def nothing(x):
	   pass
	 
	#Creamos la ventana con las trackbars:
	cv2.namedWindow('Parametros')
	cv2.createTrackbar('Hue Minimo','Parametros',10,179,nothing)
	cv2.createTrackbar('Hue Maximo','Parametros',53,179,nothing)
	cv2.createTrackbar('Saturation Minimo','Parametros',41,255,nothing)
	cv2.createTrackbar('Saturation Maximo','Parametros',227,255,nothing)
	cv2.createTrackbar('Value Minimo','Parametros',90,255,nothing)
	cv2.createTrackbar('Value Maximo','Parametros',144,255,nothing)
	cv2.createTrackbar('Kernel X', 'Parametros', 0, 30, nothing)
	cv2.createTrackbar('Kernel Y', 'Parametros', 0, 30, nothing)
	 
	 
	#Recordamos al usuario con qué tecla se sale:
	print("\nPulsa 'ESC' para salir\n")
	 
	 
	while(1):
	  #Leemos los sliders y guardamos los valores de H,S,V para construir los rangos:
	  hMin = cv2.getTrackbarPos('Hue Minimo','Parametros')
	  hMax = cv2.getTrackbarPos('Hue Maximo','Parametros')
	  sMin = cv2.getTrackbarPos('Saturation Minimo','Parametros')
	  sMax = cv2.getTrackbarPos('Saturation Maximo','Parametros')
	  vMin = cv2.getTrackbarPos('Value Minimo','Parametros')
	  vMax = cv2.getTrackbarPos('Value Maximo','Parametros')
	 
	  #Creamos los arrays que definen el rango de colores:
	  color_bajos=np.array([hMin,sMin,vMin])
	  color_altos=np.array([hMax,sMax,vMax])
	 
	  #Leemos los sliders que indican las dimensiones del Kernel:
	  kernelx = cv2.getTrackbarPos('Kernel X', 'Parametros')
	  kernely = cv2.getTrackbarPos('Kernel Y', 'Parametros')
	  
	  #Creamos el kernel:
	  kernel = np.ones((kernelx,kernely),np.uint8)
	 
	  #Detectamos los colores y eliminamos el ruido:
	  mask = cv2.inRange(hsv, color_bajos, color_altos)
	  mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
	  mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

	  
	  #Mostramos los resultados y salimos:
	  cv2.imshow('Original',img)
	  cv2.imshow('Mascara',mask)
	  k = cv2.waitKey(5) & 0xFF
	  if k == 27:
	    #img = findsold.Find_Sold(mask,img)
	    cv2.imwrite("segmentacion/"+str(i+1)+".jpg",mask)		
	    break
	cv2.destroyAllWindows()	

	data['parametros'].append({
	'Hue Minimo': hMin,
	'Hue Maximo': hMax,
	'Saturation Minimo': sMin,
	'Saturation Maximo': sMax,
	'Value Minimo': vMin,
	'Value Maximo': vMax,
	'Kernel X': kernelx,
	'Kernel Y': kernely})
	with open('data.json', 'w') as file:
    	  	  json.dump(data, file, indent=4)




 
