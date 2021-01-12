"""Read ePub metadata"""

import epub_meta


class EpubError(Exception):
    """Wrap implementation-specific errors for this module."""
    pass


def read_data(file: str) -> dict:
    """Read the metadata from given file path."""
    try:
        return epub_meta.get_epub_metadata(file, read_cover_image=False, read_toc=False)
    except Exception as e:
        raise EpubError(e)
