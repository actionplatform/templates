<?php
/**
 * Removes the plugin's options on uninstall.
 *
 * @package {{ cookiecutter.class_prefix }}
 */

if ( ! defined( 'WP_UNINSTALL_PLUGIN' ) ) {
	exit;
}

require_once __DIR__ . '/includes/class-{{ cookiecutter.project_slug }}-settings.php';

( new {{ cookiecutter.class_prefix }}_Settings() )->delete();
