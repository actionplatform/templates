<?php

namespace App\Http\Controllers;

use App\Http\Requests\StoreItemRequest;
use App\Models\Item;
use Illuminate\Http\JsonResponse;

class ItemController
{
    public function index(): JsonResponse
    {
        return response()->json(Item::query()->orderBy('id')->get());
    }

    public function store(StoreItemRequest $request): JsonResponse
    {
        $item = Item::create(['name' => $request->validated('name')]);

        return response()->json($item, 201);
    }

    public function show(Item $item): JsonResponse
    {
        return response()->json($item);
    }
}
