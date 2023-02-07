import time
from multiprocessing import Process
from os.path import basename, join

import tensorflow as tf
from detect import object_detect as det


class Inferencer(Process):

    def __init__(self, queue) -> None:
        super().__init__()
        self.queue = queue
        self.model = None

    def run(self):
        if self.model is None:
            self.model = self.load_model()
        while True:
            image = self.queue.get()
            self.infer(image, 'test.jpg')

    def load_model(self):
        return tf.saved_model.load(det.model_dir)

    def infer(self, image, save_path):
        start_time = time.time()
        prediction = det.predict(self.model, image, det.MIN_SCORE)
        print(f'Inference time: {time.time() - start_time} s')

        for prediction_box, class_id, score in zip(prediction['boxes'], prediction['classes'], prediction['scores']):
            bbox = det.tf_box_to_bbox(image, prediction_box)
            det.draw_bbox(image, bbox, det.COCO_CLASSNAMES[int(class_id)], score)

        output_path = join('.', basename(save_path))
        det.save_image(image, output_path)
        print(f'Saved annotated image to {output_path}')