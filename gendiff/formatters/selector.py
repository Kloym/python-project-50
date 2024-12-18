from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import plain_format
from gendiff.formatters.json import format_json


def select_formatter(diff_data, format_name):
    formatters = {
        "stylish": format_stylish,
        "plain": plain_format,
        "json": format_json,
    }
    formatter = formatters.get(format_name)
    if formatter:
        return formatter(diff_data)