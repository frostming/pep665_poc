# pep665_poc

A POC implementation of PEP 665

## Locker

The locker is adapted from [resolvelib's example](https://github.com/sarugaku/resolvelib/blob/master/examples/pypi_wheel_provider.py).

```
usage: pep665-lock [-h] [--marker MARKER] [--tag TAG] [--requires-python REQUIRES_PYTHON] [-o OUTFILE] [-i INFILE]

PEP 665 lock file generator

options:
  -h, --help            show this help message and exit
  --marker MARKER       Override the lock file marker(default null)
  --tag TAG             Override the lock file tag(default null)
  --requires-python REQUIRES_PYTHON
                        Override the lock file requires-python(default: ==major.minor)
  -o OUTFILE, --outfile OUTFILE
                        Write output into the given file
  -i INFILE, --infile INFILE
                        Read dependencies from the given requirements file
```

## Installer

```
usage: pep665-install [-h] -i INFILE [-v]

PEP 665 installer

options:
  -h, --help            show this help message and exit
  -i INFILE, --infile INFILE
                        Install packages from the given lock file
  -v, --verbose         See the verbose output
```

## Caveats

- Requirements with extras are not supported by this example.
- The locker is not cross-platform. Namely you must install with the same python version and environment.
