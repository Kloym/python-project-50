def find_diff(data1: dict, data2: dict):
    diff_dict = {}
    united_data = sorted(data1 | data2)
    for key in united_data:
        if key in data1 and key in data2 and data1[key] == data2[key]:
            diff_dict[key] = {
                "key": key,
                "vertex_type": "unchanged",
                "value": data1[key],
            }
        elif key not in data2:
            diff_dict[key] = {
                "key": key, "vertex_type": "removed", "value": data1[key]
                }
        elif key not in data1:
            diff_dict[key] = {
                "key": key, "vertex_type": "added", "value": data2[key]
                }
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff_dict[key] = {
                "key": key,
                "vertex_type": "nested",
                "value": find_diff(data1[key], data2[key]),
            }
        elif data1[key] != data2[key]:
            diff_dict[key] = {
                "key": key,
                "vertex_type": "changed",
                "value_old": data1[key],
                "value_new": data2[key],
            }
    return diff_dict
