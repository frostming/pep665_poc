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

## Caveats

Requirements with extras are not supported by this example.
