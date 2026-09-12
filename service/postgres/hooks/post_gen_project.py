"""Service overlay post-gen: keep only the selected provider's files."""

import shutil
from pathlib import Path

PROVIDER = "{{ cookiecutter.provider }}"

root = Path("services") / "{{ cookiecutter.service_name }}"
for item in root.iterdir():
    if item.is_dir() and item.name.startswith("_provider_"):
        if item.name == f"_provider_{PROVIDER}":
            for f in item.rglob("*"):
                if f.is_file():
                    dest = root / f.relative_to(item)
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(f, dest)
        shutil.rmtree(item)
