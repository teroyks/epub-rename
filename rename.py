"""Rename epub file.

Desired name format:
Authorlastname Author Names - Book Title.epub
"""

from pprint import pprint as pp
import argparse
import os

from epub import read_data, EpubError
from metadata_parser import first_author, format_author_name

parser = argparse.ArgumentParser(
    description='Rename an epub file based on author and title')
parser.add_argument('-p', '--print-only', action='store_true',
                    help='print out new name without renaming the file')
parser.add_argument('filename', type=str, help='epub file')

args = parser.parse_args()

try:
    metadata = read_data(args.filename)
    author = format_author_name(first_author(metadata.authors))
    old_filename, extension = os.path.splitext(args.filename)
    dir = os.path.dirname(old_filename)

    new_filename = f'{author} - {metadata.title}{extension}'
    if not args.print_only:
        os.rename(args.filename, f'{dir}/{new_filename}')
    print(new_filename)
except EpubError as e:
    print(e)
