from pathlib import Path

from {{ cookiecutter.package_name }} import __version__

ROOT = Path(__file__).resolve().parents[1]


def test_version_matches_last_version():
    expected = (ROOT / "LAST_VERSION").read_text().strip()

    assert __version__ == expected
