def hello(name: str) -> str:
    name = name.strip()

    if not name:
        raise ValueError("name is required")

    return f"hello, {name}"
