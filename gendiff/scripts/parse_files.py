import argparse
import json
import yaml

parser = argparse.ArgumentParser(
    description="Compares two configuration " "files and shows a difference."
)
parser.add_argument("first_file")
parser.add_argument("second_file")
parser.add_argument("-f", "--format", help="set format of output")


def read(path):
    with open(path) as file:
        return file.read()


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
