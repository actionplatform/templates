# frozen_string_literal: true

RSpec.describe "/api/v1/items", type: :request do
  include Client

  it "creates, lists and gets" do
    post_json "/api/v1/items", { name: "pen" }
    created = body

    expect(last_response.status).to eq(201)
    expect(created["name"]).to eq("pen")

    get "/api/v1/items"
    expect(body).to include(created)

    get "/api/v1/items/#{created['id']}"
    expect(body).to eq(created)
  end

  it "gives every error one shape" do
    post_json "/api/v1/items", { name: "  " }

    expect(last_response.status).to eq(422)
    expect(body).to eq(
      "detail" => { "code" => "invalid", "message" => "name is required", "field" => "name" }
    )

    get "/api/v1/items/999999"

    expect(last_response.status).to eq(404)
    expect(body.dig("detail", "code")).to eq("not_found")
  end
end
