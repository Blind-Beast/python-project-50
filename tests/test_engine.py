from gendiff.engine import generate_diff


def test_generate_diff():
    output = 'tests/test_data/file_out.txt'
    with open(output, 'r') as f1:
        result = f1.read()
    diff = generate_diff('tests/test_data/file1_in.json', 
                         'tests/test_data/file2_in.json')
    assert diff == result