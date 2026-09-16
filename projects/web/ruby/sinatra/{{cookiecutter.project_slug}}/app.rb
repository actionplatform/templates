# frozen_string_literal: true

require "rack"

require_relative "app/version"
require_relative "app/core/base_api"
require_relative "app/repositories/items"
require_relative "app/services/items"
require_relative "app/api/health"
require_relative "app/api/v1/items"

module App
  API_V1_PREFIX = "/api/v1"

  def self.create(item_repository: ItemRepository.new)
    item_service = ItemService.new(item_repository)

    Rack::Builder.new do
      map("/health") { run HealthApi }
      map("#{App::API_V1_PREFIX}/items") { run ItemsApi.with(item_service) }
    end
  end
end
