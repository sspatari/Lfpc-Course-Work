import json
from pprint import pprint


def getSignMatrixObj():
    with open('sign_matrix.json') as data_file:
        return json.load(data_file)

data = getSignMatrixObj()

pprint(data)
