import os

import pytest

from gendiff.engine import generate_diff

TEST_DATA_DIR = os.path.join('tests', 'test_data')


def get_file_path(filename):
    return os.path.join(TEST_DATA_DIR, filename)


def read_file(filepath):
    with open(filepath) as file:
        return file.read()


@pytest.mark.parametrize('file1_name, file2_name, formatter', [
    ('file3_in.json', 'file4_in.json', 'stylish'),
    ('file3_in.yml', 'file4_in.yml', 'stylish')
])
def test_generate_diff(file1_name, file2_name, formatter):
    output_path = get_file_path('file2_out.txt')
    expected_result = read_file(output_path)
    print(expected_result)
    file1_path = get_file_path(file1_name)
    file2_path = get_file_path(file2_name)
    actual_result = generate_diff(file1_path, file2_path, formatter)
    print(actual_result)
    assert actual_result == expected_result