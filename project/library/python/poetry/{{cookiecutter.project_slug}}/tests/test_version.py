import {{ cookiecutter.package_name }}


def test_version_is_set():
    assert {{ cookiecutter.package_name }}.__version__ == "0.1.0"
