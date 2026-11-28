<?php

namespace App\Http\Controllers;

use Illuminate\Http\JsonResponse;

class HealthController
{
    public const VERSION = '0.0.0';

    public function __invoke(): JsonResponse
    {
        return response()->json(['status' => 'ok', 'version' => self::VERSION]);
    }
}
