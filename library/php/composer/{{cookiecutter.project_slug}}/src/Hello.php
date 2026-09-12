<?php

declare(strict_types=1);

namespace {{ cookiecutter.php_namespace }};

/**
 * Dummy public class. Replace with the real API.
 */
final class Hello
{
    public static function greet(string $name = 'world'): string
    {
        return sprintf('hello, %s', $name);
    }
}
