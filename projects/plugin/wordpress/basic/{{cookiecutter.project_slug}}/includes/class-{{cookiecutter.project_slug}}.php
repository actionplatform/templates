<?php
/**
 * Plugin entry class.
 *
 * @package {{ cookiecutter.class_prefix }}
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Wires the plugin into WordPress.
 */
class {{ cookiecutter.class_prefix }} {

	public const SHORTCODE = '{{ cookiecutter.package_name }}_greeting';

	/**
	 * Settings page and option.
	 *
	 * @var {{ cookiecutter.class_prefix }}_Settings
	 */
	private {{ cookiecutter.class_prefix }}_Settings $settings;

	/**
	 * Constructor.
	 *
	 * @param {{ cookiecutter.class_prefix }}_Settings $settings Settings page and option.
	 */
	public function __construct( {{ cookiecutter.class_prefix }}_Settings $settings ) {
		$this->settings = $settings;
	}

	/**
	 * Hooks into WordPress.
	 */
	public function register(): void {
		add_action( 'admin_menu', array( $this->settings, 'add_page' ) );
		add_action( 'admin_init', array( $this->settings, 'register' ) );
		add_shortcode( self::SHORTCODE, array( $this, 'render_greeting' ) );
	}

	/**
	 * Shortcode output.
	 */
	public function render_greeting(): string {
		return esc_html( $this->settings->greeting() );
	}
}
