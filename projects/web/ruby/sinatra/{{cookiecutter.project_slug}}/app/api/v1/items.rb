# frozen_string_literal: true

require_relative "../../core/base_api"
require_relative "../../core/errors"

class ItemsApi < BaseApi
  def self.with(service)
    set :service, service

    self
  end

  get "/" do
    json settings.service.list.map(&:to_h)
  end

  post "/" do
    name = body_json.fetch("name", nil)
    raise ValidationError.new("name is required", field: "name") unless name.is_a?(String)

    status 201

    json settings.service.create(name).to_h
  end

  get "/:id" do
    id = Integer(params[:id], exception: false)
    raise NotFoundError, "item #{params[:id]} not found" if id.nil?

    json settings.service.get(id).to_h
  end
end
