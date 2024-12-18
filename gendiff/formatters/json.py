import json


def format_json(data: dict):
    return json.dumps(data, indent=2)
