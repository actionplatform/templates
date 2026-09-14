# frozen_string_literal: true

RSpec.describe ItemService do
  subject(:service) { described_class.new(ItemRepository.new) }

  it "creates and finds an item" do
    item = service.create(" pen ")

    expect(item.name).to eq("pen")
    expect(service.get(item.id)).to eq(item)
    expect(service.list).to eq([item])
  end

  it "rejects a blank name" do
    expect { service.create("  ") }.to raise_error(ValidationError) do |error|
      expect(error.field).to eq("name")
    end
  end

  it "rejects a long name" do
    expect { service.create("x" * 41) }.to raise_error(ValidationError)
  end

  it "raises when missing" do
    expect { service.get(42) }.to raise_error(NotFoundError, "item 42 not found")
  end
end
