# Demo of snapshottest bug

## Description of the bug

When running nosetests with a test class name, snapshots are not updated
when `--snapshot-update` is provided on the command line.

## Demo
Prerequisite: install Poetry (https://python-poetry.org/)

```
$ poetry install
$ ./test
```
