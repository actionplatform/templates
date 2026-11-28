<?php
/**
 * Plugin tests.
 *
 * @package {{ cookiecutter.class_prefix }}
 */

use Brain\Monkey;
use Brain\Monkey\Functions;
use Mockery\Adapter\Phpunit\MockeryPHPUnitIntegration;
use PHPUnit\Framework\TestCase;

/**
 * Hook wiring and shortcode.
 */
final class {{ cookiecutter.class_prefix }}_Test extends TestCase {

	use MockeryPHPUnitIntegration;

	/**
	 * Settings the plugin reads.
	 *
	 * @var {{ cookiecutter.class_prefix }}_Settings
	 */
	private {{ cookiecutter.class_prefix }}_Settings $settings;

	/**
	 * Subject.
	 *
	 * @var {{ cookiecutter.class_prefix }}
	 */
	private {{ cookiecutter.class_prefix }} $plugin;

	protected function setUp(): void {
		parent::setUp();
		Monkey\setUp();
		$this->settings = new {{ cookiecutter.class_prefix }}_Settings();
		$this->plugin   = new {{ cookiecutter.class_prefix }}( $this->settings );
	}

	protected function tearDown(): void {
		Monkey\tearDown();
		parent::tearDown();
	}

	public function test_register_hooks_the_settings_page(): void {
		Functions\when( 'add_shortcode' )->justReturn( true );

		$this->plugin->register();

		$this->assertNotFalse( has_action( 'admin_menu', array( $this->settings, 'add_page' ) ) );
		$this->assertNotFalse( has_action( 'admin_init', array( $this->settings, 'register' ) ) );
	}

	public function test_register_adds_the_shortcode(): void {
		Functions\expect( 'add_shortcode' )
			->once()
			->with( {{ cookiecutter.class_prefix }}::SHORTCODE, array( $this->plugin, 'render_greeting' ) );

		$this->plugin->register();
	}

	public function test_shortcode_prints_the_escaped_greeting(): void {
		Functions\when( 'get_option' )->justReturn( 'a < b' );
		Functions\when( 'esc_html' )->alias( 'htmlspecialchars' );

		$this->assertSame( 'a &lt; b', $this->plugin->render_greeting() );
	}
}
