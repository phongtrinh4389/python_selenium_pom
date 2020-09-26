import os
import json


def load_settings():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.json')) as f:
        return json.load(f)


settings = load_settings()
