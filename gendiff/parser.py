import json
import os

import yaml


def get_file_extension(filepath):
    """Return file extension"""
    _, ext = os.path.splitext(filepath)
    return ext[1:]


def get_file_content(filepath):
    """Read file content"""
    with open(filepath) as f:
        return f.read()


def parse_data(data, format):
    """Return file content depending on format"""
    if format == 'json':
        return json.loads(data)
    if format in ['yml', 'yaml']:
        return yaml.load(data, Loader=yaml.SafeLoader)
    raise ValueError(f"Unsupported file format: {format}")


def parse_data_from_file(filepath):
    """Return file content"""
    format = get_file_extension(filepath)
    content = get_file_content(filepath)
    return parse_data(content, format)