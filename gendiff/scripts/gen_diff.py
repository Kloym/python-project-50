from gendiff.scripts.parse_files import parse


def generate_diff(filepath1, filepath2):
    data1 = parse(filepath1)
    data2 = parse(filepath2)
    keys = set(data1.keys()).union(data2.keys())
    diff_lines = []

    for key in sorted(keys):
        if key in data1 and key not in data2:
            diff_lines.append(f"  - {key}: {data1[key]}")
        elif key not in data1 and key in data2:
            diff_lines.append(f"  + {key}: {data2[key]}")
        elif data1[key] != data2[key]:
            diff_lines.append(f"  - {key}: {data1[key]}")
            diff_lines.append(f"  + {key}: {data2[key]}")
        else:
            diff_lines.append(f"    {key}: {data1[key]}")
    diff_lines = '\n'.join(diff_lines)
    return diff_lines
