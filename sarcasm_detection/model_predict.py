import tensorflow as tf

model = tf.keras.models.load_model('./saved_models/bidirectional_lstm_model3')


def model_predict(sentence, threshold):
    result = 1 if model.predict(sentence) >= threshold else 0
    return result


while True:
    inp = input('Enter a sentence: ')
    pred = model_predict(inp)
    if model_predict(pred):
        print('That was Sarcasm')
    else:
        print('That was Not Sarcasm')
