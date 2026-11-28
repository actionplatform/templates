<?php

namespace Tests\Feature;

use App\Models\Item;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class ItemTest extends TestCase
{
    use RefreshDatabase;

    public function test_items_start_empty(): void
    {
        $this->getJson('/api/v1/items')->assertOk()->assertExactJson([]);
    }

    public function test_create_then_get_and_list(): void
    {
        $this->postJson('/api/v1/items', ['name' => 'first'])
            ->assertCreated()
            ->assertExactJson(['id' => 1, 'name' => 'first']);

        $this->getJson('/api/v1/items/1')
            ->assertOk()
            ->assertExactJson(['id' => 1, 'name' => 'first']);

        $this->getJson('/api/v1/items')
            ->assertOk()
            ->assertExactJson([['id' => 1, 'name' => 'first']]);
    }

    public function test_list_returns_every_item(): void
    {
        Item::factory()->count(3)->create();

        $this->getJson('/api/v1/items')->assertOk()->assertJsonCount(3);
    }

    public function test_create_rejects_blank_or_missing_name(): void
    {
        $this->postJson('/api/v1/items', ['name' => '   '])->assertUnprocessable();
        $this->postJson('/api/v1/items', [])->assertUnprocessable();
    }

    public function test_create_rejects_long_name(): void
    {
        $this->postJson('/api/v1/items', ['name' => str_repeat('a', 41)])->assertUnprocessable();
    }

    public function test_unknown_item_is_404(): void
    {
        $this->getJson('/api/v1/items/42')->assertNotFound();
        $this->getJson('/api/v1/items/abc')->assertNotFound();
    }

    public function test_validation_errors_are_json_without_an_accept_header(): void
    {
        $this->call('POST', '/api/v1/items', [], [], [], [], '{"name":""}')
            ->assertUnprocessable()
            ->assertHeader('Content-Type', 'application/json');
    }
}
