"""PEP 665 compliant lock file writer"""
import os
import tomlkit
import datetime

from tomlkit.items import AoT, DottedKey


SPEC_VERSION = "1.0"


def _filter_none(d):
    return {k: v for k, v in d.items() if v is not None}


def format_candidate(key, candidate):
    table = tomlkit.table()
    table.update(
        _filter_none(
            {
                "filename": os.path.basename(candidate.url),
                "url": candidate.url,
                "requires-python": candidate.requires_python,
                "requires": [str(dep) for dep in candidate.dependencies],
            }
        )
    )
    table.raw_append(
        DottedKey([tomlkit.key("hashes"), tomlkit.key("sha256")]),
        candidate.metadata["sha256"],
    )
    table_name = DottedKey(
        [tomlkit.key("package"), tomlkit.key(key), tomlkit.key(str(candidate.version))]
    )
    return f"\n[[{table_name.as_string()}]]\n{table.as_string()}"


def format_resolution(metadata, result):
    doc = tomlkit.document()
    doc.update(
        {
            "version": SPEC_VERSION,
            "created-at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "metadata": _filter_none(
                {
                    "marker": metadata.marker,
                    "tag": metadata.tag,
                    "requires": metadata.requires,
                    "requires-python": metadata.requires_python,
                }
            ),
        }
    )
    output = tomlkit.dumps(doc)
    for key, candidate in result.mapping.items():
        if isinstance(key, tuple):
            key = f"{key[0]}[{key[1]}]"
        output += format_candidate(key, candidate)
    # check the doc is valid
    tomlkit.parse(output)
    return output
