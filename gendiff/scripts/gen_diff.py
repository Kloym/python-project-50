from gendiff.scripts.parse_files import parse


def generate_diff(filepath1, filepath2):
    file1 = parse(filepath1)
    file2 = parse(filepath2)
    keys = sorted(set(file1.keys()) | set(file2.keys()))
    diff_lines = []
    diff_lines.append("{")

    for key in sorted(keys):
        if key in file1 and key not in file2:
            diff_lines.append(f"  - {key}: {file1[key]}")
        elif key not in file1 and key in file2:
            diff_lines.append(f"  + {key}: {file2[key]}")
        elif file1[key] != file2[key]:
            diff_lines.append(f"  - {key}: {file1[key]}")
            diff_lines.append(f"  + {key}: {file2[key]}")
        else:
            diff_lines.append(f"    {key}: {file1[key]}")
    make_json(diff_lines)
    diff_lines.append("}")
    diff_lines = "\n".join(diff_lines)
    return diff_lines


def make_json(text: list[str]):
    for i in range(len(text)):
        if "False" in text[i]:
            text[i] = text[i].replace("False", "false")
        elif "True" in text[i]:
            text[i] = text[i].replace("True", "true")
