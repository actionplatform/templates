import {
  type ArgumentsHost,
  Catch,
  type ExceptionFilter,
  HttpException,
  HttpStatus,
} from "@nestjs/common";
import type { Response } from "express";

@Catch()
export class ErrorFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const response = host.switchToHttp().getResponse<Response>();
    const { status, message } = describe(exception);

    response.status(status).json({ error: message });
  }
}

function describe(exception: unknown): { status: number; message: string } {
  if (exception instanceof HttpException) {
    return { status: exception.getStatus(), message: exception.message };
  }

  return {
    status: HttpStatus.INTERNAL_SERVER_ERROR,
    message: "internal error",
  };
}
