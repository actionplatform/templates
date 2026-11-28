# {{ cookiecutter.project_name }}

{% if cookiecutter.description %}{{ cookiecutter.description }}

{% endif %}A WordPress plugin: a settings page (Settings API) under Settings, and a `[{{ cookiecutter.package_name }}_greeting]` shortcode that prints the saved greeting.

## Run

```bash
composer install
composer build
```

`composer build` writes `dist/{{ cookiecutter.project_slug }}-<version>.zip`, with the version taken from `LAST_VERSION`. Upload it in Plugins > Add New > Upload Plugin, or unzip it into `wp-content/plugins/`.

## Test

```bash
composer test
composer lint
composer analyse
```

- `composer test`: PHPUnit with Brain Monkey, no WordPress install needed.
- `composer lint`: `php -l` on every file, then phpcs with the WordPress coding standards (`composer lint:fix` runs phpcbf).
- `composer analyse`: phpstan level 6 with `szepeviktor/phpstan-wordpress`.

## Layout

```
{{ cookiecutter.project_slug }}.php   # plugin header, constants, bootstrap
includes/                             # one class per file: plugin wiring, settings page
uninstall.php                         # removes the option when the plugin is deleted
readme.txt                            # WordPress.org readme, goes into the zip
scripts/build.php                     # builds the distributable zip
tests/                                # PHPUnit + Brain Monkey
.code_quality/                        # phpcs (WordPress), phpstan, phpunit
```
