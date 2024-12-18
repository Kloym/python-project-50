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
