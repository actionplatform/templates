from {{ cookiecutter.package_name }} import hello


def test_hello_default():
    assert hello() == "hello, world"


def test_hello_name():
    assert hello("ana") == "hello, ana"
