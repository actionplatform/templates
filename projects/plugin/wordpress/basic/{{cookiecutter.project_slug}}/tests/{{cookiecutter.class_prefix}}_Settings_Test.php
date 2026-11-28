<?php
/**
 * Settings tests.
 *
 * @package {{ cookiecutter.class_prefix }}
 */

use Brain\Monkey;
use Brain\Monkey\Functions;
use Mockery\Adapter\Phpunit\MockeryPHPUnitIntegration;
use PHPUnit\Framework\TestCase;

/**
 * Settings page and option.
 */
final class {{ cookiecutter.class_prefix }}_Settings_Test extends TestCase {

	use MockeryPHPUnitIntegration;

	/**
	 * Subject.
	 *
	 * @var {{ cookiecutter.class_prefix }}_Settings
	 */
	private {{ cookiecutter.class_prefix }}_Settings $settings;

	protected function setUp(): void {
		parent::setUp();
		Monkey\setUp();
		$this->settings = new {{ cookiecutter.class_prefix }}_Settings();
	}

	protected function tearDown(): void {
		Monkey\tearDown();
		parent::tearDown();
	}

	public function test_register_declares_the_option(): void {
		Functions\stubTranslationFunctions();
		Functions\expect( 'register_setting' )
			->once()
			->with( {{ cookiecutter.class_prefix }}_Settings::GROUP, {{ cookiecutter.class_prefix }}_Settings::OPTION, \Mockery::type( 'array' ) );
		Functions\expect( 'add_settings_section' )->once();
		Functions\expect( 'add_settings_field' )->once();

		$this->settings->register();
	}

	public function test_add_page_lives_under_settings(): void {
		Functions\expect( 'add_options_page' )
			->once()
			->with( \Mockery::any(), \Mockery::any(), 'manage_options', {{ cookiecutter.class_prefix }}_Settings::PAGE, \Mockery::type( 'array' ) );

		$this->settings->add_page();
	}

	public function test_sanitize_cleans_the_value(): void {
		Functions\when( 'sanitize_text_field' )->alias( 'trim' );

		$this->assertSame( 'Hi', $this->settings->sanitize( '  Hi ' ) );
	}

	public function test_sanitize_falls_back_to_the_default(): void {
		Functions\when( 'sanitize_text_field' )->alias( 'trim' );

		$this->assertSame( {{ cookiecutter.class_prefix }}_Settings::DEFAULT, $this->settings->sanitize( '   ' ) );
		$this->assertSame( {{ cookiecutter.class_prefix }}_Settings::DEFAULT, $this->settings->sanitize( array( 'x' ) ) );
	}

	public function test_greeting_reads_the_option(): void {
		Functions\expect( 'get_option' )
			->once()
			->with( {{ cookiecutter.class_prefix }}_Settings::OPTION, {{ cookiecutter.class_prefix }}_Settings::DEFAULT )
			->andReturn( 'Olá' );

		$this->assertSame( 'Olá', $this->settings->greeting() );
	}

	public function test_greeting_falls_back_when_the_option_is_empty(): void {
		Functions\when( 'get_option' )->justReturn( '' );

		$this->assertSame( {{ cookiecutter.class_prefix }}_Settings::DEFAULT, $this->settings->greeting() );
	}

	public function test_delete_removes_the_option(): void {
		Functions\expect( 'delete_option' )->once()->with( {{ cookiecutter.class_prefix }}_Settings::OPTION );

		$this->settings->delete();
	}

	public function test_render_page_is_closed_to_users_without_the_capability(): void {
		Functions\expect( 'current_user_can' )->once()->with( 'manage_options' )->andReturn( false );
		Functions\expect( 'settings_fields' )->never();

		ob_start();
		$this->settings->render_page();

		$this->assertSame( '', ob_get_clean() );
	}

	public function test_render_page_prints_the_form(): void {
		Functions\when( 'current_user_can' )->justReturn( true );
		Functions\when( 'get_admin_page_title' )->justReturn( 'Title' );
		Functions\when( 'esc_html' )->returnArg();
		Functions\expect( 'settings_fields' )->once()->with( {{ cookiecutter.class_prefix }}_Settings::GROUP );
		Functions\expect( 'do_settings_sections' )->once()->with( {{ cookiecutter.class_prefix }}_Settings::PAGE );
		Functions\expect( 'submit_button' )->once();

		ob_start();
		$this->settings->render_page();
		$html = (string) ob_get_clean();

		$this->assertStringContainsString( '<h1>Title</h1>', $html );
		$this->assertStringContainsString( 'options.php', $html );
	}

	public function test_render_field_escapes_the_value(): void {
		Functions\when( 'get_option' )->justReturn( '"><b>' );
		Functions\when( 'esc_attr' )->alias( 'htmlspecialchars' );

		ob_start();
		$this->settings->render_field();
		$html = (string) ob_get_clean();

		$this->assertStringNotContainsString( '<b>', $html );
		$this->assertStringContainsString( 'name="{{ cookiecutter.package_name }}_greeting"', $html );
	}
}
