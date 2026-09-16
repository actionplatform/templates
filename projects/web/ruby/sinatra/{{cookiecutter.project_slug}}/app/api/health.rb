# frozen_string_literal: true

require_relative "../core/base_api"
require_relative "../schemas/health"
require_relative "../version"

class PingApi < BaseApi
  get "/" do
    json Health.new(status: "ok", version: App::VERSION).to_h
  end
end
