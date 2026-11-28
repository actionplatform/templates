<?php
/**
 * Plugin Name:       {{ cookiecutter.project_name }}
 * Plugin URI:        https://{{ cookiecutter.__domain }}/{{ cookiecutter.__owner }}/{{ cookiecutter.project_slug }}
 * Description:{% if cookiecutter.description %}       {{ cookiecutter.description }}{% endif %}
 * Version:           0.0.0
 * Requires at least: 6.5
 * Requires PHP:      {{ cookiecutter._php_version }}
 * Author:            {{ cookiecutter.author or cookiecutter.__owner }}
 * License:           {{ cookiecutter.__spdx or 'GPL-2.0-or-later' }}
 * Text Domain:       {{ cookiecutter.project_slug }}
 *
 * @package {{ cookiecutter.class_prefix }}
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( '{{ cookiecutter.package_name|upper }}_VERSION', '0.0.0' );
define( '{{ cookiecutter.package_name|upper }}_FILE', __FILE__ );

require_once __DIR__ . '/includes/class-{{ cookiecutter.project_slug }}-settings.php';
require_once __DIR__ . '/includes/class-{{ cookiecutter.project_slug }}.php';

( new {{ cookiecutter.class_prefix }}( new {{ cookiecutter.class_prefix }}_Settings() ) )->register();
