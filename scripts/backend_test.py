import backend
import unittest
import numpy as np
import glob
import datetime
class test_load_files(unittest.TestCase):
    def test_read_files(self):
        image = backend.load_files("quiron.png","","").read_image()
        self.assertEqual(type(image).__name__,'ndarray')

    def test_load_model(self):
        model = backend.load_files("quiron.png","","").load_model()
        self.assertEqual(model,True)


class test_capacitor_detector(unittest.TestCase):
    def test_resize(self):
        image = backend.load_files("quiron.png","","").read_image()
        model = backend.load_files("quiron.png","","").load_model()
        pimage = backend.capacitor_detector(image,model).resize(image)
        self.assertEqual(type(pimage).__name__,'ndarray')


    def test_detect_capacitor(self):
        image = backend.load_files("quiron.png","","").read_image()
        model = backend.load_files("quiron.png","","").load_model()
        coords = backend.capacitor_detector(image,model).detect_capacitor()
        self.assertEqual(coords.tolist(),np.zeros((20,4)).tolist())


class test_output_files(unittest.TestCase):
    def test_create_txt(self):
        backend.output_files(np.zeros((20,4))).create_txt()

        self.assertEqual('/home/david/Projects/Aplicaciones/AIVA_2021_CapaDect/scripts/{}.txt'.format(datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")) in glob.glob("/home/david/Projects/Aplicaciones/AIVA_2021_CapaDect/scripts/*txt"),True)


if __name__=="__main__":
    unittest.main()