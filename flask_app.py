from flask import Flask, request, jsonify

import model_class

app = Flask(__name__)

detector = model_class.SarcasmDetector()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/infer', methods=["POST"])
def infer():
    data = request.form
    sentence = data['sentence']
    label = detector.infer(sentence)
    res = jsonify({'label': label})
    return res
