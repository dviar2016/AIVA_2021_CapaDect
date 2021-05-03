import cv2
import numpy as np
import datetime
import os
import pathlib
import matplotlib
import matplotlib.pyplot as plt
import os
import random
import io
import imageio
import glob
import scipy.misc
from six import BytesIO
from PIL import Image, ImageDraw, ImageFont
import tensorflow as tf
# from object_detection.utils import label_map_util
from object_detection.utils import config_util
# from object_detection.utils import visualization_utils as viz_utils
# from object_detection.utils import colab_utils
from object_detection.builders import model_builder




class load_files():

    def __init__(self,image_path=None):
        self.image_path = image_path


    def read_image(self):


        img_data = tf.io.gfile.GFile(self.image_path, 'rb').read()
        image = Image.open(BytesIO(img_data))
        (im_width, im_height) = image.size
        return np.array(image.getdata()).reshape(
            (im_height, im_width, 3)).astype(np.uint8)


    def load_model(self):
        tf.keras.backend.clear_session()

        print('Building model and restoring weights for fine-tuning...', flush=True)
        num_classes = 1
        pipeline_config = 'efficientdet_d7_coco17_tpu-32/pipeline.config'
        checkpoint_path = 'efficientdet_d7_coco17_tpu-32/checkpoint/ckpt-0'


        configs = config_util.get_configs_from_pipeline_file(pipeline_config)
        model_config = configs['model']
        model_config.ssd.num_classes = num_classes
        model_config.ssd.freeze_batchnorm = True
        self.detection_model = model_builder.build(
            model_config=model_config, is_training=True)

        fake_box_predictor = tf.compat.v2.train.Checkpoint(
            _base_tower_layers_for_heads=self.detection_model._box_predictor._base_tower_layers_for_heads,
            # _prediction_heads=detection_model._box_predictor._prediction_heads,
            #    (i.e., the classification head that we *will not* restore)
            _box_prediction_head=self.detection_model._box_predictor._box_prediction_head,
        )
        fake_model = tf.compat.v2.train.Checkpoint(
            _feature_extractor=self.detection_model._feature_extractor,
            _box_predictor=fake_box_predictor)
        ckpt = tf.compat.v2.train.Checkpoint(model=fake_model)
        ckpt.restore(checkpoint_path).expect_partial()

        # Run model through a dummy image so that variables are created
        image, shapes = self.detection_model.preprocess(tf.zeros([1, 1536, 1536, 3]))
        prediction_dict = self.detection_model.predict(image, shapes)
        _ = self.detection_model.postprocess(prediction_dict, shapes)

        weights = np.load("final.npz",allow_pickle=True)["arr_0"]

        self.detection_model.set_weights(weights)



        print("model loaded")
        print('Weights restored!')


        return self.detection_model




class preprocessing_image():
    def __init__(self):
        pass
    def resize(self,image):
        image = cv2.resize(image,(1536,1536))
        cv2.imwrite("prueba.png",image)
        return image




class capacitor_detector(preprocessing_image):

    def __init__(self,image,detection_model):
        super().__init__()

        self.image = image
        self.detection_model = detection_model

        self.pimage = self.resize(self.image)


    def detect_capacitor(self):


        self.pimage = np.expand_dims(
                self.pimage, axis=0)

        # Again, uncomment this decorator if you want to run inference eagerly
        @tf.function
        def detect(input_tensor):

            preprocessed_image, shapes = self.detection_model.preprocess(input_tensor)
            prediction_dict = self.detection_model.predict(preprocessed_image, shapes)
            return self.detection_model.postprocess(prediction_dict, shapes)

        # Note that the first frame will trigger tracing of the tf.function, which will
        # take some time, after which inference should be fast.

        label_id_offset = 1

        input_tensor = tf.convert_to_tensor(self.pimage, dtype=tf.float32)
        detections = detect(input_tensor)

        return detections['detection_boxes'][0].numpy(),detections['detection_scores'][0].numpy()



class output_files():

    def __init__(self,coords):
        self.coords = coords


    def create_txt(self):
        file = open('{}.txt'.format(datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")), "w")
        for row in self.coords:
            file.write(str(row))
            file.write("\n")

        file.close()




class detection_warning():
    def message_error(self):
        print("Not enough capacitors were detected")



    def __init__(self):
        pass

