import cv2
import numpy as np
#Le code mange la webcam
cap = cv2.VideoCapture(0)
while(1):       
#Lecture de l'image
    _, img = cap.read()
#création de l'echelle de couleur
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
#création du mask qui permettra de "détecter" la couleur qui a été définie plus haut
    mask = cv2.inRange(hsv, lower_red, upper_red)
#renseigne le pixel sur lequel il y a la couleur rouge qui sera détectée par le mask
    res = cv2.bitwise_and(img,img, mask= mask)
#ouverture des fenêtres qui vont nous montrer le flux de la webcam, le mask qui est 
#en noir et blanc et les pixels rouges qui ont étés détectés sur le flux de la cam (grâce au mask)
    cv2.imshow('img',img)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
#Si on appuie sur la touche qui est renseignée dans "ord('q')", cela ferme toute les fenêtres qui ont étés ouvertes par le code
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#ferme toutes les fenêtres qui ont étés ouvertes par le programme et désactivation de la recupération du flux de la caméra
cv2.destroyAllWindows()
cap.release()