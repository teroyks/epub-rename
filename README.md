# EPUB Rename

This is a simple script that renames an EPUB file based on book metadata (author name and book title).

The filename format is `Lastname Firstnames - Book title.epub`.

## Installation

The script uses [Pipenv](https://pipenv.pypa.io/en/latest/) to handle package dependencies, so installing Pipenv is a prerequisite.

1. Download the repository into a local directory
2. Go to the repository directory
3. Run `pipenv install` to install the packages used by the script

You can test that the installation was successful by running `pipenv run pytest`.

## Usage

After installation, you can run the script in the project directory:

```python
pipenv run python rename.py PATH_TO_EPUB_FILE
```

With the `-p` option, the command outputs the new filename but does not rename the file.

```python
pipenv run python rename.py -p PATH_TO_EPUB_FILE
```

### With Helper Script

You can create a helper script that will load the correct environment and allow running the script from anywhere.

For this you need to know the project directory and the virtual environment path:

- type `pwd` in the project directory to get the project diretory
- type `pipenv --venv` to show the virtual environment path

Now, create a script (for example `epub-rename`) somewhere in your path with the following contents (replace `PROJECT_DIRECTORY` and `PIPENV_DIRECTORY` with the real directories from above):

```shell
#!/bin/bash

DIR="PROJECT_DIRECTORY"
source "PIPENV_DIRECTORY/bin/activate"
PYTHONPATH="$DIR/src" python "$DIR/rename.py" $@
```

Make the script executable (`chmod u+x epub-rename`). Now you can run the rename from 
anywhere with `epub-rename FILE`.

## Acknowledgements

The script uses [epub-meta](https://github.com/paulocheque/epub-meta) by Paulo Cheque to read the EPUB metadata.
