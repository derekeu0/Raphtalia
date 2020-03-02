import json
from collections import namedtuple

def get(file):
    with open(file,encoding='utf8') as f:
        return json.load(f,object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))