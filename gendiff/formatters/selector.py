from gendiff.formatters.json import format_json
from gendiff.formatters.plain import plain_format
from gendiff.formatters.stylish import format_stylish


def select_formatter(diff_data, format_name):
    formatters = {"stylish": format_stylish,
                  "plain": plain_format,
                  "json": format_json
                  }
    return formatters[format_name](diff_data)
