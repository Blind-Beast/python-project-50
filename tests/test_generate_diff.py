import os

import pytest

from gendiff.generate_diff import generate_diff

TEST_DATA_DIR = os.path.join('tests', 'test_data')


def get_file_path(filename):
    return os.path.join(TEST_DATA_DIR, filename)


def get_expected_result(filename):
    expected_result_path = get_file_path(filename)
    with open(expected_result_path) as file:
        return file.read()


@pytest.mark.parametrize('file1_name, file2_name, formatter, expected_file', [
    ('file1.json', 'file2.json', 'stylish', 'expected_stylish.txt'),
    ('file1.yml', 'file2.yml', 'stylish', 'expected_stylish.txt'),
    ('file1.json', 'file2.json', 'plain', 'expected_plain.txt'),
    ('file1.yml', 'file2.yml', 'plain', 'expected_plain.txt'),
    ('file1.json', 'file2.json', 'json', 'expected_json.txt'),
    ('file1.yml', 'file2.yml', 'json', 'expected_json.txt')
])
def test_generate_diff(file1_name, file2_name, formatter, expected_file):
    expected_result = get_expected_result(expected_file)
    file1_path = get_file_path(file1_name)
    file2_path = get_file_path(file2_name)
    actual_result = generate_diff(file1_path, file2_path, formatter)
    assert actual_result == expected_result


@pytest.mark.parametrize('file1_name, file2_name, formatter', [
    ('file1.json', 'file3.txt', 'stylish'),
    ('file2.yml', 'file3.txt', 'stylish'),
    ('file1.json', 'file3.txt', 'plain'),
    ('file2.yml', 'file3.txt', 'plain'),
    ('file1.json', 'file3.txt', 'json'),
    ('file2.yml', 'file3.txt', 'json')
])
def test_unsupported_formatter(file1_name, file2_name, formatter):
    file1_path = get_file_path(file1_name)
    file2_path = get_file_path(file2_name)
    with pytest.raises(ValueError):
        generate_diff(file1_path, file2_path, formatter)