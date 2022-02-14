import pickle
import tensorflow as tf

from keras.preprocessing.sequence import pad_sequences

max_length = 200
trunc_type = 'post'
padding_type = 'post'

with open("tokenizer_data.pkl", 'rb') as handle:
    data = pickle.load(handle)
    tokenizer = data['tokenizer']
    vocab_size = data['vocab_size']
model = tf.keras.models.load_model('/saved_models/bidirectional_lstm_model2')


def model_predict(sentence, threshold):
    sequences = tokenizer.texts_to_sequences(sentence)
    padded = pad_sequences(sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)
    result = 1 if model.predict(padded) >= threshold else 0
    return result


import random


def dummy_predict():
    return random.randint(0, 1)


while True:
    inp = input('Enter a sentence: ')
    pred = dummy_predict(inp)
    print(pred)
    if dummy_predict(pred):
        print('That was Sarcasm')
    else:
        print('That was Not Sarcasm')