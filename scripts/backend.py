import cv2
import numpy as np
import datetime
class load_files(): #Esta clase permite cargar archivos necesarios para el funcionamiento del programa principal

    def __init__(self,image_path,model_path,weights_path):
        self.image_path = image_path
        self.model_path = model_path
        self.weights_path = weights_path

    def read_image(self): # Se lee la imagen sobre la cual se desean detectar condensadores
        image=cv2.imread(self.image_path,1)
        return image

    def load_model(path_network): # Se carga el modelo de red de deteccion entrenado.
        print("model loaded")

        return True
    def load_weights(path_weights): # Se cargan los pesos de la red aprendidos durante el proceso de entrenamiento.
        print("weights loaded")
        return True



class preprocessing_image(): # Clase base que se inicializa en la definicion de su clase hija, trata el preprocesamiento de la imagen.
    def __init__(self):
        pass
    def resize(self,image):

        return cv2.resize(image,None,fx=0.5,fy=0.5)




class capacitor_detector(preprocessing_image): # Clase derivada de preprocessing_image donde se realiza la inferencia del modelo sobre la imagen preprocesada. 

    def __init__(self,image,model):
        super().__init__()

        self.image = image #imagen
        self.model = model #modelo cargado

        self.pimage = self.resize(self.image) #imagen preprocesada

    def detect_capacitor(self): #Dado que la arquitectura y entrenamiento de la red esta en proceso esto es un definicion basica de la funcion.
        print("Inference model")
        return np.zeros((20,4))



class output_files(): #Almacenamiento de la lista de tuplas que devuelva la clase capacitor detector, lo que se suele llamar ROI. 

    def __init__(self,coords):
        self.coords = coords


    def create_txt(self):
        file = open('{}'.format(datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")), "w")#Permite guardar el archivo con un nombre distinto segun su tiempo de creacion, 
                                                                                             # para que no se sobrescriban entre si, al llegar distintas placas.
        for row in self.coords:
            file.write(str(row))
            file.write("\n")

        file.close()




class detection_warning(): # Clase que funciona como "alarma" si se detecta un fallo en la deteccion
    def message_error(self):
        print("Not enough capacitors were detected")

    def __init__(self):
        pass

