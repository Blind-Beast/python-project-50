def generate_added(key, value):
    """Generate structure for added keys"""
    return {
        'tag': 'added',
        'key': key,
        'value': value
    }


def generate_deleted(key, value):
    """Generate structure for deleted keys"""
    return {
        'tag': 'deleted',
        'key': key,
        'value': value
    }


def generate_nested(key, value1, value2):
    """Generate structure for nested keys"""
    return {
        'tag': 'nested',
        'key': key,
        'children': generate(value1, value2)
    }


def generate_changed(key, value1, value2):
    """Generate structure for changed keys"""
    return {
        'tag': 'changed',
        'key': key,
        'old_value': value1,
        'new_value': value2
    }


def generate_unchanged(key, value):
    """Generate structure for unchanged keys"""
    return {
        'tag': 'unchanged',
        'key': key,
        'value': value
    }


def generate(data1, data2):
    """Generate difference between two datasets"""
    keys = data1.keys() | data2.keys()
    added = data2.keys() - data1.keys()
    deleted = data1.keys() - data2.keys()
    diff = []
    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if key in added:
            diff.append(generate_added(key, value2))
        elif key in deleted:
            diff.append(generate_deleted(key, value1))
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.append(generate_nested(key, value1, value2))
        elif value1 != value2:
            diff.append(generate_changed(key, value1, value2))
        else:
            diff.append(generate_unchanged(key, value1))
    sorted_diff = sorted(diff, key=lambda x: x['key'])
    return sorted_diff
