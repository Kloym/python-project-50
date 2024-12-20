def format_value_plain(value):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if not isinstance(value, dict):
        if value is None:
            return 'null'
        elif isinstance(value, str):
            return f"'{value}'"
        elif type(value) in [bool, int, float]:
            return str(value).lower()
    else:
        return '[complex value]'


def plain_format(data: dict, path=""):
    lines = []
    for k, v in data.items():
        current_path = path + v['key'] + '.'
        if v['vertex_type'] == 'nested':
            lines.append(f'{plain_format(v["value"], current_path)}')
        elif v['vertex_type'] == 'changed':
            lines.append(f"Property '{path}{k}' was updated. "
                         f"From {format_value_plain(v['value_old'])}"
                         f" to {format_value_plain(v['value_new'])}")
        if v['vertex_type'] == 'added':
            lines.append(f"Property '{path}{k}'"
                         f" was added with value:"
                         f" {format_value_plain(v['value'])}")
        elif v['vertex_type'] == 'removed':
            lines.append(f"Property '{path}{k}' was removed")

    return '\n'.join(lines)
