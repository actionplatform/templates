# frozen_string_literal: true

class DomainError < StandardError
  STATUS = 400
  CODE = "domain_error"

  attr_reader :field

  def initialize(message, field: nil)
    super(message)
    @field = field
  end

  def status = self.class::STATUS

  def as_detail
    detail = { code: self.class::CODE, message: message }
    detail[:field] = field unless field.nil?

    detail
  end
end

class NotFoundError < DomainError
  STATUS = 404
  CODE = "not_found"
end

class ValidationError < DomainError
  STATUS = 422
  CODE = "invalid"
end

class ConflictError < DomainError
  STATUS = 409
  CODE = "conflict"
end
