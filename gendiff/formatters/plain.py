def format_value_plain(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    if isinstance(value, (int, float)) or value == "0":
        return str(value)
    return f"'{value}'"


def plain_format(data: dict, prefix=''):
    result = []
    for key, value in data.items():
        print(f'{data=}')
        status = value['vertex_type']
        current_prefix = prefix + value['key'] + '.'
        if status == 'nested':
            result.append(f'{plain_format(value['value'], current_prefix)}')
        elif status == 'changed':
            result.append(f"Property '{prefix}{key}' was updated. "
                          f"From {format_value_plain(value['value_old'])}"
                          f" to {format_value_plain(value['value_new'])}")
        if status == 'added':
            result.append(f"Property '{prefix}{key}'"
                          f" was added with value:"
                          f" {format_value_plain(value['value'])}")
        elif status == 'removed':
            result.append(f"Property '{prefix}{key}' was removed")
    return '\n'.join(result)
