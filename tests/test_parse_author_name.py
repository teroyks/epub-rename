"""Test author name parsing."""

from metadata_parser import first_author


def test_parse_first_author():
    assert first_author(['Foo Bar', 'Bar Baz']
                        ) == 'Foo Bar', 'Should pick first name from a list.'


def test_one_author():
    assert first_author(['Foo Bar']) == 'Foo Bar', 'Should pick the only name.'


def test_no_authors():
    assert first_author([]) == 'Unknown', 'Should handle empty authors list.'


def test_comma_separated():
    assert first_author(
        ['Foo, Bar']) == 'Foo', 'Should recognize comma-separated list as author name.'


def test_authors_list_unchanged():
    authors = ['foo']
    first_author(authors)
    assert authors == ['foo'], 'Should not mutate parameter list.'
