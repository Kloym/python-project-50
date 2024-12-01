import json
import argparse
import yaml


parser = argparse.ArgumentParser(
    description="Compares two configuration " "files and shows a difference."
)
parser.add_argument("first_file")
parser.add_argument("second_file")
parser.add_argument("-f", "--format", help="set format of output")


def get_file_format(file_name):
    return file_name.split(".")[-1]


def parse(data):
    extension = get_file_format(data)
    if extension == "json":
        with open(data) as file:
            return json.load(file)
    elif extension in ("yaml", "yml"):
        with open(data, "r") as file:
            return yaml.safe_load(file)
