import argparse
import sys

from .locker import lock

PYTHON_VERSION = f"{sys.version_info.major}.{sys.version_info.minor}"


def lock_main():
    parser = argparse.ArgumentParser(
        "pep665-lock", description="PEP 665 lock file generator"
    )
    parser.add_argument("--marker", help="Override the lock file marker(default null)")
    parser.add_argument("--tag", help="Override the lock file tag(default null)")
    parser.add_argument(
        "--requires-python",
        dest="requires_python",
        default=f"=={PYTHON_VERSION}",
        help="Override the lock file requires-python(default: ==major.minor)",
    )
    parser.add_argument("-o", "--outfile", help="Write output into the given file")
    parser.add_argument(
        "-i",
        "--infile",
        help="Read dependencies from the given requirements file",
        default="requirements.txt",
    )
    return lock(parser.parse_args())
