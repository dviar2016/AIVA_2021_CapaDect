import backend
import numpy as np
import glob
class Application():

    def __init__(self):
        self.image_path = ""
        self.dependencies = backend.load_files()

        self.model = self.dependencies.load_model()

    def main(self,image_path):
        self.dependencies.image_path =image_path
        self.image = self.dependencies.read_image()


        inference_model = backend.capacitor_detector(self.image,self.model)
        roi,roi_score = inference_model.detect_capacitor()
        roi_index = np.argwhere(roi_score>0.25)
        print(roi_index)

        roi = roi[roi_index]
        if len(roi) >= 15:
            backend.output_files(roi).create_txt()

        else:
            backend.detection_warning().message_error()



if __name__=="__main__":
    image_path = glob.glob("images/*.jpg")
    aplication = Application()
    for i in image_path:
        aplication.main(i)