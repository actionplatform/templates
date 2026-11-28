<?php
/**
 * PHPUnit bootstrap.
 *
 * @package {{ cookiecutter.class_prefix }}
 */

define( 'ABSPATH', __DIR__ . '/' );

require_once dirname( __DIR__ ) . '/vendor/autoload.php';
require_once dirname( __DIR__ ) . '/includes/class-{{ cookiecutter.project_slug }}-settings.php';
require_once dirname( __DIR__ ) . '/includes/class-{{ cookiecutter.project_slug }}.php';
