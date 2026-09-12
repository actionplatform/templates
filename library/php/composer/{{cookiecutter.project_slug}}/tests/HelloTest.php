<?php

declare(strict_types=1);

namespace {{ cookiecutter.php_namespace }}\Tests;

use PHPUnit\Framework\TestCase;
use {{ cookiecutter.php_namespace }}\Hello;

final class HelloTest extends TestCase
{
    public function testDefault(): void
    {
        $this->assertSame('hello, world', Hello::greet());
    }

    public function testName(): void
    {
        $this->assertSame('hello, ana', Hello::greet('ana'));
    }
}
