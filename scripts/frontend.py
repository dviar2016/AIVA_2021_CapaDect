
import backend

class Application():

    def __init__(self,image_path,model_path,weights_path):
        self.image_path = image_path
        self.model_path = model_path
        self.weights_path = weights_path

    def main(self):
        x = backend.load_files(self.image_path,self.model_path,self.weights_path)
        image = x.read_image()
        model = x.load_model()
        weights = x.load_weights()

        inference_model = backend.capacitor_detector(image,model)
        roi = inference_model.detect_capacitor()

        if len(roi) >= 15:
            backend.output_files(roi).create_txt()

        else:
            backend.detection_warning().message_error()



Application("quiron.png","","").main()