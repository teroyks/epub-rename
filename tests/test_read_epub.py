"""Test reading epub metadata."""

import os
import pytest

from epub import read_data, EpubError


def test_file_not_found():
    with pytest.raises(EpubError):
        read_data('this-file-does-not-exist')


@pytest.fixture
def epub_file():
    """Return path to a test epub file."""
    file = os.path.dirname(os.path.realpath(__file__)) + '/Test Book.epub'
    assert os.path.isfile(file), 'Test ebook file should exist.'
    return file


def test_read_metadata(epub_file):
    epub_data = read_data(epub_file)
    assert epub_data.title == 'Test Book'
    assert epub_data.authors == [
        'Adam Author'], 'Should list authors as an array.'
