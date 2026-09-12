"""Keep only the CI config selected in `ci`; stamp the package dir into unrendered workflows."""

import shutil
from pathlib import Path

CI = "{{ cookiecutter.ci }}"
PACKAGE_DIR = "{{ cookiecutter.package_name }}"

FILES = {
    "github": [".github"],
    "gitlab": [".gitlab-ci.yml"],
    "bitbucket": ["bitbucket-pipelines.yml"],
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

for workflow in Path(".github/workflows").glob("*.yml") if Path(".github").exists() else []:
    workflow.write_text(workflow.read_text().replace("PACKAGE_DIR", PACKAGE_DIR))
