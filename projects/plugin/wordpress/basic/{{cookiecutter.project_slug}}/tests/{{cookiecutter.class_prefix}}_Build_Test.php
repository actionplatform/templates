<?php
/**
 * Build script tests.
 *
 * @package {{ cookiecutter.class_prefix }}
 */

use PHPUnit\Framework\TestCase;

/**
 * The distributable zip.
 */
final class {{ cookiecutter.class_prefix }}_Build_Test extends TestCase {

	/**
	 * Output directory.
	 *
	 * @var string
	 */
	private string $out;

	protected function setUp(): void {
		parent::setUp();
		$this->out = sys_get_temp_dir() . '/{{ cookiecutter.project_slug }}-build-' . uniqid();
	}

	protected function tearDown(): void {
		$files = glob( $this->out . '/*' );
		foreach ( false === $files ? array() : $files as $file ) {
			unlink( $file );
		}
		if ( is_dir( $this->out ) ) {
			rmdir( $this->out );
		}
		parent::tearDown();
	}

	public function test_build_writes_a_zip_with_the_plugin_files(): void {
		$root = dirname( __DIR__ );
		exec( 'php ' . escapeshellarg( $root . '/scripts/build.php' ) . ' ' . escapeshellarg( $this->out ), $lines, $code );

		$this->assertSame( 0, $code );

		$version = trim( (string) file_get_contents( $root . '/LAST_VERSION' ) );
		$zip     = new ZipArchive();
		$this->assertTrue( $zip->open( $this->out . '/{{ cookiecutter.project_slug }}-' . $version . '.zip' ) );

		$main = (string) $zip->getFromName( '{{ cookiecutter.project_slug }}/{{ cookiecutter.project_slug }}.php' );
		$this->assertStringContainsString( 'Version:           ' . $version, $main );
		$this->assertStringContainsString( "'{{ cookiecutter.package_name|upper }}_VERSION', '" . $version . "'", $main );

		$this->assertNotFalse( $zip->locateName( '{{ cookiecutter.project_slug }}/includes/class-{{ cookiecutter.project_slug }}.php' ) );
		$this->assertNotFalse( $zip->locateName( '{{ cookiecutter.project_slug }}/uninstall.php' ) );
		$this->assertNotFalse( $zip->locateName( '{{ cookiecutter.project_slug }}/readme.txt' ) );
		$this->assertFalse( $zip->locateName( '{{ cookiecutter.project_slug }}/tests/bootstrap.php' ) );
		$this->assertFalse( $zip->locateName( '{{ cookiecutter.project_slug }}/composer.json' ) );
		$zip->close();
	}
}
