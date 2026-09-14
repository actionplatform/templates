# frozen_string_literal: true

module Client
  include Rack::Test::Methods

  def app
    @app ||= App.create
  end

  def body
    JSON.parse(last_response.body)
  end

  def post_json(path, payload)
    post path, JSON.generate(payload), { "CONTENT_TYPE" => "application/json" }
  end
end
