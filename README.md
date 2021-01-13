# Demo of snapshottest bug

## Description of the bug

When running nosetests with a test class name, snapshots are not updated
when `--snapshot-update` is provided on the command line:

```
# this works
$ nosetests --snapshot-update path/to/test_file.py

# this doesn't
$ nosetests --snapshot-update path/to/test_file.py:TestClass
```

## Demo
Prerequisite: install Poetry (https://python-poetry.org/)

```
$ poetry install
$ ./test
```
