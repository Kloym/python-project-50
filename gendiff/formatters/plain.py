def format_value_plain(value):
    if not isinstance(value, dict):
        if value is None:
            return 'null'
        elif isinstance(value, str):
            return "'{0}'".format(value)
        elif isinstance(value, bool):
            return str(value).lower()
        elif isinstance(value, int):
            return f"'{value}'"
    else:
        return '[complex value]'


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
