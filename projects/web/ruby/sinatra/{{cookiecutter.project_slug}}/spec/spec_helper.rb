# frozen_string_literal: true

ENV["RACK_ENV"] = "test"

require "rack/test"
require "json"
require_relative "../app"
require_relative "support/client"

RSpec.configure do |config|
  config.expect_with(:rspec) { |c| c.syntax = :expect }
  config.disable_monkey_patching!
  config.order = :random
end
