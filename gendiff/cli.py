import argparse


def parse_arguments():
    """Return data from the options specified in command-line"""
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f", "--format",
        default='stylish',
        help="set format of output",
    )
    return parser.parse_args()