# frozen_string_literal: true

require "json"
require "sinatra/base"
require "sinatra/json"

require_relative "errors"

class BaseApi < Sinatra::Base
  helpers Sinatra::JSON

  set :show_exceptions, false
  set :raise_errors, false

  before { content_type :json }

  error DomainError do
    exc = env["sinatra.error"]
    status exc.status

    json detail: exc.as_detail
  end

  not_found do
    json detail: { code: "not_found", message: "route not found" }
  end

  def body_json
    JSON.parse(request.body.read)
  rescue JSON::ParserError
    raise ValidationError.new("body is not valid JSON", field: "body")
  end
end
