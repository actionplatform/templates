# frozen_string_literal: true

RSpec.describe "GET /ping", type: :request do
  include Client

  it "answers with the version" do
    get "/ping"

    expect(last_response.status).to eq(200)
    expect(body).to eq("status" => "ok", "version" => App::VERSION)
  end
end
