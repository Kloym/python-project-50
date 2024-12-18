import itertools


def format_stylish(diff: dict, replacer=" ", space_counts=2):

    def walk(data, depth=0):
        indent = replacer * space_counts * (depth + 1)
        indent_for_changed = indent * space_counts
        lines = []
        for k, v in data.items():
            if v["vertex_type"] == "nested":
                lines.append(
                    f"{indent_for_changed}"
                    f'{k}: {walk(v["value"], depth + 1)}'
                )
            elif v["vertex_type"] == "unchanged":
                lines.append(f'{indent}{build_line(v, "value", depth)}')
            elif v["vertex_type"] == "changed":
                lines.append(f"{indent}"
                             f'{build_line(v, "value_old", depth, "- ")}')
                lines.append(f"{indent}"
                             f'{build_line(v, "value_new", depth, "+ ")}')
            elif v["vertex_type"] == "added":
                lines.append(f'{indent}{build_line(v, "value", depth, "+ ")}')
            elif v["vertex_type"] == "removed":
                lines.append(f'{indent}{build_line(v, "value", depth, "- ")}')
        result = itertools.chain("{", lines, ["    " * depth + "}"])
        return "\n".join(result)

    return walk(diff, 0)


def build_line(data, key, depth, prefix="  "):
    line = (
        f'{"  " * depth}{prefix}{data["key"]}:'
        f" {_stylish_format(data[key], depth + 1)}"
    )
    return line


def _stylish_format(value, depth, replacer=" ", space_counts=4):
    if isinstance(value, dict):
        line = []
        for k, v in value.items():
            indent = replacer * space_counts * (depth + 1)
            line.append(f"\n{indent}{k}: {_stylish_format(v, depth + 1)}")
        result = itertools.chain("{", line, "\n", ["    " * depth, "}"])
        return "".join(result)
    else:
        if value is None:
            return "null"
        elif isinstance(value, bool):
            return str(value).lower()
        return str(value)
