SPACE = " "
ADD = '+ '
DELETE = '- '
NONE = '  '


def convert_to_str(value, spaces_count=2):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
        indent = SPACE * (spaces_count + 4)
        lines = []
        for key, inner_value in value.items():
            formatted_value = convert_to_str(inner_value, spaces_count + 4)
            lines.append(f"{indent}{NONE}{key}: {formatted_value}")
        formatted_string = '\n'.join(lines)
        end_indent = SPACE * (spaces_count + 2)
        return f"{{\n{formatted_string}\n{end_indent}}}"
    return f"{value}"


def format_diff_stylish(diff, spaces_count=2):
    indent = SPACE * spaces_count
    lines = []
    for item in diff:
        key_name = item['key']
        old_value = convert_to_str(item.get("old_value"), spaces_count)
        new_value = convert_to_str(item.get("new_value"), spaces_count)
        current_value = convert_to_str(item.get('value'), spaces_count)
        tag = item.get('tag')
        if tag == 'unchanged':
            lines.append(f"{indent}{NONE}{key_name}: {current_value}")
        elif tag == 'changed':
            lines.append(f"{indent}{DELETE}{key_name}: {old_value}")
            lines.append(f"{indent}{ADD}{key_name}: {new_value}")
        elif tag == 'deleted':
            lines.append(f"{indent}{DELETE}{key_name}: {current_value}")
        elif tag == 'added':
            lines.append(f"{indent}{ADD}{key_name}: {current_value}")
        elif tag == 'nested':
            children = format_diff_stylish(
                item.get('children'), spaces_count + 4
            )
            lines.append(f"{indent}{NONE}{key_name}: {children}")
    formatted_string = '\n'.join(lines)
    end_indent = SPACE * (spaces_count - 2)
    return f"{{\n{formatted_string}\n{end_indent}}}"