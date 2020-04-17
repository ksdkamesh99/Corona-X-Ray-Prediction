import json
FILE_NAME="corona-data.json"
def save(x):
    with open(FILE_NAME, 'w') as f:
        json.dump(x, f)


def load():
    res = {}
    with open(FILE_NAME, 'r') as f:
        res = json.load(f)
    return res