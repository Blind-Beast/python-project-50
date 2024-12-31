import argparse
import json
import os

import yaml


def parse_arguments():
    """Return data from the options specified in command-line"""
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f", "--format",
        default='stylish',
        help="set format of output",
    )
    return parser.parse_args()


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


def parse_data_from_file(filepath):
    """Return file content"""
    format = get_file_extension(filepath)
    content = get_file_content(filepath)
    return parse_data(content, format)