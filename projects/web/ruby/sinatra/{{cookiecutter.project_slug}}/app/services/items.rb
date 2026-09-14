# frozen_string_literal: true

require_relative "../core/errors"

class ItemService
  MAX_NAME = 40

  def initialize(repository)
    @repository = repository
  end

  def list
    @repository.list
  end

  def get(id)
    item = @repository.get(id)
    raise NotFoundError, "item #{id} not found" if item.nil?

    item
  end

  def create(name)
    name = name.strip
    raise ValidationError.new("name is required", field: "name") if name.empty?

    if name.length > MAX_NAME
      raise ValidationError.new("name is longer than #{MAX_NAME} characters", field: "name")
    end

    @repository.add(name)
  end
end
