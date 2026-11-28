<?php

declare(strict_types=1);

$root    = dirname(__DIR__);
$slug    = '{{ cookiecutter.project_slug }}';
$out     = $argv[1] ?? $root . '/dist';
$version = trim((string) file_get_contents($root . '/LAST_VERSION'));
$files   = ['{{ cookiecutter.project_slug }}.php', 'uninstall.php', 'readme.txt', 'LICENSE'];

if (preg_match('/^\d+\.\d+\.\d+$/', $version) !== 1) {
    fwrite(STDERR, "LAST_VERSION is not a version: $version\n");
    exit(1);
}

foreach (glob($root . '/includes/*.php') ?: [] as $include) {
    $files[] = 'includes/' . basename($include);
}

if (!is_dir($out) && !mkdir($out, 0777, true)) {
    fwrite(STDERR, "cannot create $out\n");
    exit(1);
}

$target = "$out/$slug-$version.zip";

if (is_file($target)) {
    unlink($target);
}

$zip = new ZipArchive();

if ($zip->open($target, ZipArchive::CREATE) !== true) {
    fwrite(STDERR, "cannot write $target\n");
    exit(1);
}

foreach ($files as $file) {
    $path = "$root/$file";

    if (!is_file($path)) {
        continue;
    }

    $content = (string) file_get_contents($path);

    if ($file === "$slug.php") {
        $content = (string) preg_replace('/^( \* Version:\s+)\S+/m', '${1}' . $version, $content);
        $content = (string) preg_replace("/(_VERSION', ')[^']*'/", '${1}' . $version . "'", $content);
    }

    $zip->addFromString("$slug/$file", $content);
}

$zip->close();

echo $target . "\n";
