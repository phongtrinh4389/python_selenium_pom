import os
import json


def load_json(json_filename):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), json_filename)) as f:
        return json.load(f)


searched_location_data_list = load_json('searched_location_data.json')
