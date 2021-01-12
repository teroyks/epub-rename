"""Rename epub file.

Desired name format:
Authorlastname Author Names - Book Title.epub
"""

import argparse
import os

from epub import read_data, EpubError
from metadata_parser import format_file_name

parser = argparse.ArgumentParser(
    description='Rename an epub file based on author and title')
parser.add_argument('-p', '--print-only', action='store_true',
                    help='print out new name without renaming the file')
parser.add_argument('filename', type=str, help='epub file')

args = parser.parse_args()

try:
    metadata = read_data(args.filename)

    dir = os.path.dirname(args.filename)
    _, extension = os.path.splitext(args.filename)

    new_filename = format_file_name(metadata) + extension

    if not args.print_only:
        os.rename(args.filename, f'{dir}/{new_filename}')

    print(new_filename)
except EpubError as e:
    print(e)
    exit(1)
