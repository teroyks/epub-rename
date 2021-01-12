"""Rename epub file.

Desired name format:
Authorlastname Author Names - Book Title.epub
"""

import argparse
import os
from pathlib import Path

from epub import read_data, EpubError
from metadata_parser import format_file_name

parser = argparse.ArgumentParser(
    description='Rename an epub file based on author and title')
parser.add_argument('-p', '--print-only', action='store_true',
                    help='print out new name without renaming the file')
parser.add_argument('filename', type=str, help='epub file')

args = parser.parse_args()

try:
    file = Path(args.filename)
    metadata = read_data(file)

    new_filename = format_file_name(metadata) + file.suffix

    if not args.print_only:
        os.rename(file, file.parent / new_filename)

    print(new_filename)
except EpubError as e:
    print(e)
    exit(1)
