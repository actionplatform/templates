# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Install

```bash
composer require {{ cookiecutter.github_owner }}/{{ cookiecutter.project_slug }}
```

## Develop

```bash
composer install
composer test
composer lint
composer analyse
```

## Layout

```
src/            # PSR-4: {{ cookiecutter.php_namespace }}\
tests/          # PHPUnit
.code_quality/  # phpcs (PSR12) + phpstan
```
