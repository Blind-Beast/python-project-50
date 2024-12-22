#!/usr/bin/env python3

from gendiff import parser
from gendiff.engine import generate_diff


def main():
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)
    

if __name__ == '__main__':
    main()