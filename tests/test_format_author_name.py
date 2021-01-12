"""Test author name formatting into Lastname Firstnames."""

from metadata_parser import format_author_name


def test_format_empty_name():
    assert format_author_name('') == '', 'Should handle an empty name.'


def test_format_one_part_name():
    assert format_author_name(
        'Foo') == 'Foo', 'Should not modify a name with only one part.'


def test_format_two_part_name():
    assert format_author_name('First Last') == 'Last First'


def test_format_multipart_name():
    assert format_author_name('First Middle Last') == 'Last First Middle'
