import {
  HttpException,
  HttpStatus,
  type ValidationError,
} from "@nestjs/common";

export function validationError(errors: ValidationError[]): HttpException {
  const messages = errors.flatMap((error) =>
    Object.values(error.constraints ?? {})
  );
  const message = [...new Set(messages)].join("; ");

  return new HttpException(message, HttpStatus.UNPROCESSABLE_ENTITY);
}
