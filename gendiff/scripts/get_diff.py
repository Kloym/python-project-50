from gendiff.scripts.parse_files import parse
from gendiff.scripts.gen_diff import find_diff
from gendiff.formatters.selector import select_formatter


def generate_diff(file1, file2, format_name="stylish"):
    dict1 = parse(file1)
    dict2 = parse(file2)
    dict_diff = find_diff(dict1, dict2)
    return select_formatter(dict_diff, format_name)
