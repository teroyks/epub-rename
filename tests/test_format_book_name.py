"""Test creating a book file name."""

import pytest

from metadata_parser import format_file_name


@pytest.fixture
def sample_metadata():
    from types import SimpleNamespace
    metadata = {
        'authors': ['Foo Bar'],
        'title': 'My Book',
    }
    return SimpleNamespace(**metadata)


def test_format_file_name(sample_metadata):
    filename = format_file_name(sample_metadata)
    assert filename == 'Bar Foo - My Book'
