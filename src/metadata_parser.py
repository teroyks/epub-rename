"""Methods for parsing ebook metadata."""


def parse_list_as_name(author: str) -> str:
    """Pick first author if name is in fact a list.

    Some epubs put a comma-separated list (in error) as author name.
    """
    return author.split(',')[0]


def first_author(authors_list: list) -> str:
    """Pick the first author name from a list."""
    return parse_list_as_name(authors_list[0]) if authors_list else 'Unknown'


def format_author_name(fullname: str) -> str:
    """Format author name from First Last to Last First (with best guess)."""
    names = fullname.split(' ')
    return ' '.join(names[-1:] + names[:-1])


def format_file_name(metadata) -> str:
    """Format book file name.

    metadata must be accessible with dot notation
    and contain 'authors' and 'title' properties
    """
    author = format_author_name(first_author(metadata.authors))
    return f'{author} - {metadata.title}'
