import itertools
import sys

from packaging.tags import (
    Tag,
    compatible_tags,
    cpython_tags,
    generic_tags,
    interpreter_name,
    interpreter_version,
)


def get_supported_tags():
    py_version = sys.version_info
    interpreter = f"{interpreter_name()}{interpreter_version()}"
    is_cpython = interpreter_name() == "cp"
    if is_cpython:
        yield from cpython_tags(py_version)
    else:
        yield from generic_tags(interpreter)
    yield from compatible_tags(py_version, interpreter)


def validate_wheel_tag(wheel_tag):
    pyversions, abis, platforms = wheel_tag.split("-")
    file_tags = {
        Tag(x, y, z)
        for x, y, z in itertools.product(
            pyversions.split("."), abis.split("."), platforms.split(".")
        )
    }
    return not file_tags.isdisjoint(get_supported_tags())
