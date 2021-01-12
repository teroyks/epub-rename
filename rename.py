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
parser.add_argument('filename', type=str, help='epub file')

args = parser.parse_args()

try:
    metadata = read_data(args.filename)
    author = format_author_name(first_author(metadata.authors))
    _, extension = os.path.splitext(args.filename)

    new_filename = f'{author} - {metadata.title}{extension}'
    pp(new_filename)
except EpubError as e:
    print(e)
