import json


def format_diff_json(diff):
    """Format difference in json"""
    return json.dumps(diff, indent=4, separators=(',', ': '))