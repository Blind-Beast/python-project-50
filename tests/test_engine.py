import os

import pytest

from gendiff.engine import generate_diff

TEST_DATA_DIR = os.path.join('tests', 'test_data')


def get_file_path(filename):
    return os.path.join(TEST_DATA_DIR, filename)


def read_file(filepath):
    with open(filepath) as file:
        return file.read()


@pytest.mark.parametrize('file1_name, file2_name', [
    ('file1_in.json', 'file2_in.json'),
    ('file1_in.yml', 'file2_in.yml')
])
def test_generate_diff(file1_name, file2_name):
    output_path = get_file_path('file_out.txt')
    expected_result = read_file(output_path)
    file1_path = get_file_path(file1_name)
    file2_path = get_file_path(file2_name)
    actual_result = generate_diff(file1_path, file2_path)
    assert actual_result == expected_result