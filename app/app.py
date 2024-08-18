from flask import Flask, render_template, request, jsonify
from corenlp import *
app = Flask(__name__)

@app.get('/')
def index():
	return render_template('index.html')

@app.post('/annotate/tokens')
def annotate_tokens():
	data = request.get_json()
	input_text = data.get('text', '')
	output_text = get_tokens(input_text)
	return {'message': 'CoreNLP Tokenization: \n' + output_text}

@app.post('/annotate/split')
def annotate_ssplit():
	data = request.get_json()
	input_text = data.get('text', '')
	output_text = split_sentences(input_text)
	return {'message': 'CoreNLP Sentence Split: \n' + output_text}

@app.post('/annotate/pos')
def annotate_pos():
	data = request.get_json()
	input_text = data.get('text', '')
	output_text = parts_of_speech(input_text)
	return {'message': 'CoreNLP Parts of Speech tagging: \n' + output_text}

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)