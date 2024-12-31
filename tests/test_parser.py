import json

import pytest
from test_engine import get_expected_result

from gendiff.parser import parse_data_from_file


@pytest.fixture
def input_file_path(request):
    return request.param


@pytest.fixture
def expected_result(request):
    return get_expected_result(request.param)


@pytest.mark.parametrize('input_file_path, expected_result', [
    ('tests/test_data/file1.json', 'expected_parse_file1.json'),
    ('tests/test_data/file1.yml', 'expected_parse_file1.json'),
    ('tests/test_data/file2.json', 'expected_parse_file2.json'),
    ('tests/test_data/file2.yml', 'expected_parse_file2.json')
], indirect=['input_file_path', 'expected_result'])
def test_parse_data_from_file(input_file_path, expected_result):
    actual_data = parse_data_from_file(input_file_path)
    assert actual_data == json.loads(expected_result)