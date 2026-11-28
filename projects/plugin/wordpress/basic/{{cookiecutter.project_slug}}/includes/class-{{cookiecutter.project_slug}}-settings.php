<?php
/**
 * Settings page.
 *
 * @package {{ cookiecutter.class_prefix }}
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Registers the option and renders the page under Settings.
 */
class {{ cookiecutter.class_prefix }}_Settings {

	public const OPTION  = '{{ cookiecutter.package_name }}_greeting';
	public const GROUP   = '{{ cookiecutter.package_name }}_settings';
	public const PAGE    = '{{ cookiecutter.project_slug }}';
	public const DEFAULT = 'Hello, world';

	/**
	 * Adds the page under Settings.
	 */
	public function add_page(): void {
		add_options_page(
			'{{ cookiecutter.project_name }}',
			'{{ cookiecutter.project_name }}',
			'manage_options',
			self::PAGE,
			array( $this, 'render_page' )
		);
	}

	/**
	 * Registers the setting, its section and its field.
	 */
	public function register(): void {
		register_setting(
			self::GROUP,
			self::OPTION,
			array(
				'type'              => 'string',
				'default'           => self::DEFAULT,
				'sanitize_callback' => array( $this, 'sanitize' ),
			)
		);

		add_settings_section( 'main', '', '__return_empty_string', self::PAGE );

		add_settings_field(
			self::OPTION,
			__( 'Greeting', '{{ cookiecutter.project_slug }}' ),
			array( $this, 'render_field' ),
			self::PAGE,
			'main',
			array( 'label_for' => self::OPTION )
		);
	}

	/**
	 * Cleans the submitted greeting; an empty one falls back to the default.
	 *
	 * @param mixed $value Submitted value.
	 */
	public function sanitize( $value ): string {
		$clean = sanitize_text_field( is_scalar( $value ) ? (string) $value : '' );

		return '' === $clean ? self::DEFAULT : $clean;
	}

	/**
	 * Stored greeting, or the default.
	 */
	public function greeting(): string {
		$value = get_option( self::OPTION, self::DEFAULT );

		return is_string( $value ) && '' !== $value ? $value : self::DEFAULT;
	}

	/**
	 * Removes the option.
	 */
	public function delete(): void {
		delete_option( self::OPTION );
	}

	/**
	 * Prints the greeting input.
	 */
	public function render_field(): void {
		printf(
			'<input type="text" class="regular-text" id="%1$s" name="%1$s" value="%2$s" />',
			esc_attr( self::OPTION ),
			esc_attr( $this->greeting() )
		);
	}

	/**
	 * Prints the settings page.
	 */
	public function render_page(): void {
		if ( ! current_user_can( 'manage_options' ) ) {
			return;
		}

		echo '<div class="wrap"><h1>' . esc_html( get_admin_page_title() ) . '</h1>';
		echo '<form action="options.php" method="post">';
		settings_fields( self::GROUP );
		do_settings_sections( self::PAGE );
		submit_button();
		echo '</form></div>';
	}
}
