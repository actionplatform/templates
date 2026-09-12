# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Install

```bash
composer require {{ cookiecutter.github_owner }}/{{ cookiecutter.project_slug }}
```

## Usage

```php
use {{ cookiecutter.php_namespace }}\Hello;

Hello::greet('ana'); // "hello, ana"
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
