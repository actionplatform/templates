<?php

namespace Tests\Feature;

use App\Http\Controllers\HealthController;
use Tests\TestCase;

class HealthTest extends TestCase
{
    public function test_health_reports_ok_and_version(): void
    {
        $this->getJson('/health')
            ->assertOk()
            ->assertExactJson(['status' => 'ok', 'version' => HealthController::VERSION]);
    }
}
