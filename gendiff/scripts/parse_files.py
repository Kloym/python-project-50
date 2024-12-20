import json
import yaml
import argparse


parser = argparse.ArgumentParser(
    description="Compares two configuration " "files and shows a difference."
)


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
