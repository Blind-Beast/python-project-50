from gendiff.formatter import format_diff
from gendiff.parser import parse_data_from_file


def form_added(key, value):
    return {
        'tag': 'added',
        'key': key,
        'value': value
    }


def form_deleted(key, value):
    return {
        'tag': 'deleted',
        'key': key,
        'value': value
    }


def form_nested(key, value1, value2):
    return {
        'tag': 'nested',
        'key': key,
        'children': generate(value1, value2)
    }


def form_changed(key, value1, value2):
    return {
        'tag': 'changed',
        'key': key,
        'old_value': value1,
        'new_value': value2
    }


def form_unchanged(key, value):
    return {
        'tag': 'unchanged',
        'key': key,
        'value': value
    }


def generate(data1, data2):
    keys = data1.keys() | data2.keys()
    added = data2.keys() - data1.keys()
    deleted = data1.keys() - data2.keys()
    diff = []
    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if key in added:
            diff.append(form_added(key, value2))
        elif key in deleted:
            diff.append(form_deleted(key, value1))
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.append(form_nested(key, value1, value2))
        elif value1 != value2:
            diff.append(form_changed(key, value1, value2))
        else:
            diff.append(form_unchanged(key, value1))
    sorted_diff = sorted(diff, key=lambda x: x['key'])
    return sorted_diff


def generate_diff(first_file, second_file, formatter='stylish'):
    file1 = parse_data_from_file(first_file)
    file2 = parse_data_from_file(second_file)
    diff = generate(file1, file2)
    return format_diff(diff, formatter)
