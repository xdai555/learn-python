import json
import urllib.request

def request(action, **params):
    return {'action': action, 'params': params, 'version': 6}

# def invoke(action, **params):
#     requestJson = json.dumps(request(action, **params)).encode('utf-8')
#     print(requestJson)
#     response = json.load(urllib.request.urlopen(urllib.request.Request('http://localhost:8765', requestJson)))
#     if len(response) != 2:
#         raise Exception('response has an unexpected number of fields')
#     if 'error' not in response:
#         raise Exception('response is missing required error field')
#     if 'result' not in response:
#         raise Exception('response is missing required result field')
#     if response['error'] is not None:
#         raise Exception(response['error'])
#     return response['result']

# invoke('createDeck', deck='test2')
# result = invoke('deckNames')
# print('got list of decks: {}'.format(result))

url = 'http://localhost:8765'



import requests
def invoke(action, **params):
    requestJson = json.dumps(request(action, **params))
    ret = requests.post(url=url,data=requestJson)
    return ret.content

res = invoke('deckNames',)
print(res)
