import requests

url = 'http://corenlp:9000/'

def get_tokens(str):
    response = requests.post(url, data=str, params={'properties':'{"annotators":"tokenize","outputFormat":"json"}'})
    return response.text

def split_sentences(str):
    response = requests.post(url, data=str, params={'properties':'{"annotators":"ssplit","outputFormat":"json"}'})
    return response.text

def parts_of_speech(str):
    response = requests.post(url, data=str, params={'properties':'{"annotators":"pos","outputFormat":"json"}'})
    return response.text