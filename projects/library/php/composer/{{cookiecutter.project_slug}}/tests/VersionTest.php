<?php

declare(strict_types=1);

namespace {{ cookiecutter.php_namespace }}\Tests;

use PHPUnit\Framework\TestCase;
use {{ cookiecutter.php_namespace }}\Version;

final class VersionTest extends TestCase
{
    public function testVersionMatchesLastVersion(): void
    {
        $expected = trim((string) file_get_contents(__DIR__ . '/../LAST_VERSION'));
        $this->assertSame($expected, Version::VERSION);
    }
}
