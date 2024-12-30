import os

import pytest

from gendiff.engine import generate_diff

TEST_DATA_DIR = os.path.join('tests', 'test_data')


def get_file_path(filename):
    return os.path.join(TEST_DATA_DIR, filename)


def get_expected_result(filename):
    fixture_path = get_file_path(filename)
    with open(fixture_path) as file:
        return file.read()


@pytest.mark.parametrize('file1_name, file2_name, formatter', [
    ('file1_in.json', 'file2_in.json', 'stylish'),
    ('file1_in.yml', 'file2_in.yml', 'stylish'),
    ('file1_in.json', 'file2_in.json', 'plain'),
    ('file1_in.yml', 'file2_in.yml', 'plain')
])
def test_generate_diff(file1_name, file2_name, formatter):
    expected_result = get_expected_result(f'expected_{formatter}.txt')
    file1_path = get_file_path(file1_name)
    file2_path = get_file_path(file2_name)
    actual_result = generate_diff(file1_path, file2_path, formatter)
    assert actual_result == expected_result