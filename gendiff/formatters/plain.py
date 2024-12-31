def convert_to_str(value):
    """Convert data to string"""
    if isinstance(value, dict):
        return '[complex value]'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def format_diff_plain_item(item, path=''):
    """Format item in plain"""
    current_key = item.get('key')
    current_path = f"{path}.{current_key}" if path else current_key
    tag = item.get('tag')
    old_value = convert_to_str(item.get("old_value"))
    new_value = convert_to_str(item.get("new_value"))
    current_value = convert_to_str(item.get('value'))
    if tag == 'changed':
        return (
            f"Property '{current_path}' was updated. "
            f"From {old_value} to {new_value}"
        )
    if tag == 'deleted':
        return f"Property '{current_path}' was removed"
    if tag == 'added':
        return (
            f"Property '{current_path}' "
            f"was added with value: {current_value}"
        )
    if tag == 'nested':
        children = item.get('children')
        return format_diff_plain(children, current_path)
    return None


def format_diff_plain(diff, path=''):
    """Format difference in plain"""
    lines = []
    for item in diff:
        formatted_item = format_diff_plain_item(item, path)
        if formatted_item is not None:
            lines.append(formatted_item)
    return '\n'.join(lines)
