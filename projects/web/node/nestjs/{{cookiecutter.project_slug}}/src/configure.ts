import { type INestApplication, ValidationPipe } from "@nestjs/common";

import { ErrorFilter } from "./common/error.filter.js";
import { validationError } from "./common/validation-error.js";

export function configureApp(app: INestApplication): void {
  app.useGlobalFilters(new ErrorFilter());
  app.useGlobalPipes(
    new ValidationPipe({
      transform: true,
      whitelist: true,
      exceptionFactory: validationError,
    })
  );
}
