import json
import yaml

def get_file_format(file_name):
    return file_name.split(".")[-1]

def parse(file_path):
    extension = get_file_format(file_path)
    if extension == "json":
        with open(file_path) as file:
            return json.load(file)
    elif extension in ("yaml", "yml"):
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
