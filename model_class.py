import os
import tensorflow as tf

MODEL_DIRECTORY = os.getenv('MODEL_DIRECTORY')
MODEL_PATH = os.path.join(MODEL_DIRECTORY, 'sarcasm_model', '1')


class SarcasmDetector:
    def __init__(self):
        self.saved_path = MODEL_PATH
        self.model = tf.keras.models.load_model(self.saved_path)
        self.predict = self.model.predict

    def infer(self, sentence, threshold=0.7):
        probability = self.predict([sentence])[0][0]
        result = 1 if probability >= threshold else 0
        return result
