"""Methods for parsing ebook metadata."""


def first_author(authors_list: list) -> str:
    """Pick the first author name from a list."""
    return authors_list[0] if authors_list else 'Unknown'


def format_author_name(fullname: str) -> str:
    """Format author name from First Last to Last First (with best guess)."""
    names = fullname.split(' ')
    return ' '.join(names[-1:] + names[:-1])
