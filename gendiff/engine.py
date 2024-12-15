import json


def generate_diff(first_file, second_file):
    file1 = json.load(open(first_file))
    file2 = json.load(open(second_file))
    output = "{\n"
    for key in sorted(file1 | file2):
        if key in file1 and key in file2:
            if file1[key] == file2[key]:
                output += f'  {key}: {file1[key]}\n'
            else:
                output += f'- {key}: {file1[key]}\n+ {key}: {file2[key]}\n'
        elif key in file1 and key not in file2:
            output += f'- {key}: {file1[key]}\n'
        else:
            output += f'+ {key}: {file2[key]}\n'
    output += '}'
    return output
