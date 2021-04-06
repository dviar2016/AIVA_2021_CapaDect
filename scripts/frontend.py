import backend

#La Clase Application contiene la ejecución global del programa, llamando a las diferentes clases de backend
class Application():

    def __init__(self,image_path,model_path,weights_path):
        self.image_path = image_path
        self.model_path = model_path
        self.weights_path = weights_path
    
    #La método main va a realizar las llamadas a los diferentes métodos de las clases de backend.
    def main(self):
        
        # Se genera una instancia de la clase para posteriormente llamar a diferentes métodos de la clase load_files.
        files_instance = backend.load_files(self.image_path,self.model_path,self.weights_path)
        image = files_instance.read_image()
        model = files_instance.load_model()
        weights = files_instance.load_weights()
        # Se llama a la clase capacitor detector, la cual recibe por herencia la clase preprocessing. Finalmente se llama al método detect_capacitor.
        inference_model = backend.capacitor_detector(image,model)
        roi = inference_model.detect_capacitor() #En proceso de desarrollo
        
        # Se propone una condición para alertar si el número de condensadores es menor que 15 o almacenar en un txt las coordenadas en caso contrario.
        if len(roi) >= 15:
            #Se llama a la clase output_files y se ejecuta el  único método create_txt, el cual no recibe argumentos.
            backend.output_files(roi).create_txt()

        else:
            
            #Se llama a la clase de alertas detection_warning y al método message_error. No reciben argumentos ninguna de las dos estructuras.
            backend.detection_warning().message_error()


#Creacion de la instancia de la clases Application, recibe las rutas de la imagen, modelo y pesos.
Application("quiron.png","","").main()
