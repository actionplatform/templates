# frozen_string_literal: true

require_relative "../schemas/items"

class ItemRepository
  def initialize
    @rows = {}
    @last_id = 0
  end

  def list
    @rows.values
  end

  def get(id)
    @rows[id]
  end

  def add(name)
    @last_id += 1
    item = Item.new(id: @last_id, name: name)
    @rows[item.id] = item

    item
  end
end
