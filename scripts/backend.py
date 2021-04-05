import cv2
import numpy as np
import datetime
class load_files():

    def __init__(self,image_path,model_path,weights_path):
        self.image_path = image_path
        self.model_path = model_path
        self.weights_path = weights_path

    def read_image(self):
        image=cv2.imread(self.image_path,1)
        return image

    def load_model(path_network):
        print("model loaded")

        return True
    def load_weights(path_weights):
        print("weights loaded")
        return True



class preprocessing_image():
    def __init__(self):
        pass
    def resize(self,image):

        return cv2.resize(image,None,fx=0.5,fy=0.5)




class capacitor_detector(preprocessing_image):

    def __init__(self,image,model):
        super().__init__()

        self.image = image
        self.model = model

        self.pimage = self.resize(self.image)

    def detect_capacitor(self):
        print("Inference model")
        return np.zeros((20,4))



class output_files():

    def __init__(self,coords):
        self.coords = coords


    def create_txt(self):
        file = open('{}'.format(datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")), "w")
        for row in self.coords:
            file.write(str(row))
            file.write("\n")

        file.close()




class detection_warning():
    def message_error(self):
        print("Not enough capacitors were detected")

    def __init__(self):
        pass

