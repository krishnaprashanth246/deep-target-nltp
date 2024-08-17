import requests

url = 'http://corenlp:9000/'

def get_tokens(str):
    response = requests.post(url, data=str, params={'properties':'{"annotators":"tokenize,pos","outputFormat":"json"}'})
    return response.text