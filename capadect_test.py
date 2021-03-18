import unittest
import capadect_mockup as cd

class test_capacitor_detector(unittest.TestCase):
    def test_read_image(self):
        self.instance=cd.capacitor_detector("/image")
        self.image=self.instance.read_image()
        self.assertEqual(self.image,True)

    def test_detect_capacitor(self):
        self.instance = cd.capacitor_detector("/image")
        self.coordenates=self.instance.detect_capacitor()
        self.assertEqual(self.coordenates,(10, 50, 25, 78))

    def test_create_txt(self):
        self.instance = cd.capacitor_detector("/image")
        self.saved_txt=self.instance.create_txt()
        self.assertEqual(self.saved_txt,True)


class test_preprocessing_image(unittest.TestCase):
    def test_resize(self):
        self.image=cd.capacitor_detector("/image").read_image()
        self.instance=cd.preprocessing_image(self.image)
        self.resize_image=self.instance.resize()
        self.assertEqual(self.resize_image,True)




if __name__=="__main__":
    unittest.main()

