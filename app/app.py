from flask import Flask, render_template, request, jsonify
from corenlp import *
app = Flask(__name__)

@app.get('/')
def index():
	return render_template('index.html')

@app.post('/annotate')
def annotate():
	data = request.get_json()
	input_text = data.get('text', '')
	output_text = get_tokens(input_text)
	return {'message': 'CoreNLP output: \n' + output_text}

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)