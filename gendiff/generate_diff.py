from gendiff.formatters import format_diff
from gendiff.generator import generate
from gendiff.parser import parse_data_from_file


def generate_diff(first_file, second_file, formatter='stylish'):
    """Generate difference between two files 
    and displays it in the selected format"""
    file1 = parse_data_from_file(first_file)
    file2 = parse_data_from_file(second_file)
    diff = generate(file1, file2)
    return format_diff(diff, formatter)