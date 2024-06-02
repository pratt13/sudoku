import json, sys, os
from jsonschema import validate
from math import sqrt

current_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)


def json_parser(file):
    with open(file, "r") as f:
        data = json.load(f)
    return data


def validate_json(schema, obj):
    return validate(instance=obj, schema=schema)


def is_square(number):
    root = int(sqrt(number))
    return root * root == number
