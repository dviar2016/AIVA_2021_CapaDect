
class capacitor_detector():
    def __init__(self,image_path):
        self.image_path=image_path
        self.image=self.read_image()
        self.pimage=preprocessing_image(self.image).img
        self.coordenates=self.detect_capacitor()
        self.create_txt()
    def read_image(self):

        print("The image has been read successfully")
        return True

    def detect_capacitor(self):

        return (10, 50, 25, 78)

    def create_txt(self):

        print("txt file was created")

class preprocessing_image():
    def __init__(self,img):
        self.img=img
        self.resize()

    def resize(self):
        print('The image was resized successfully')



capacitor_detector("/image")