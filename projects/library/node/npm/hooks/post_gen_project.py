"""Keep only the CI config selected in `ci`."""

import shutil
from pathlib import Path

CI = "{{ cookiecutter.ci }}"

FILES = {
    "github": [".github"],
    "gitlab": [".gitlab-ci.yml"],
    "jenkins": ["Jenkinsfile"],
}

for provider, paths in FILES.items():
    if provider == CI:
        continue
    for p in paths:
        path = Path(p)
        if path.is_dir():
            shutil.rmtree(path)
        elif path.exists():
            path.unlink()
