<?php

declare(strict_types=1);

namespace {{ cookiecutter.php_namespace }}\Tests;

use PHPUnit\Framework\TestCase;
use {{ cookiecutter.php_namespace }}\Version;

final class VersionTest extends TestCase
{
    public function testVersionIsSet(): void
    {
        $this->assertSame('0.1.0', Version::VERSION);
    }
}
