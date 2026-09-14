from pathlib import Path

import {{ cookiecutter.package_name }}


def test_version_matches_last_version():
    expected = (Path(__file__).resolve().parents[1] / "LAST_VERSION").read_text().strip()
    assert {{ cookiecutter.package_name }}.__version__ == expected
