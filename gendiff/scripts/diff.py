from gendiff.formatters.selector import select_formatter
from gendiff.scripts.gen_diff import find_diff
from gendiff.scripts.parse_files import parse


def find(file1_path, file2_path, format_name="stylish"):
    dict1 = parse(file1_path)
    dict2 = parse(file2_path)
    diff_dict = find_diff(dict1, dict2)
    return select_formatter(diff_dict, format_name)
