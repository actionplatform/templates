import { Transform } from "class-transformer";
import { IsString, MaxLength, MinLength } from "class-validator";

export const MAX_NAME = 40;

export class CreateItemDto {
  @Transform(({ value }: { value: unknown }) =>
    typeof value === "string" ? value.trim() : value
  )
  @IsString({ message: "name is required" })
  @MinLength(1, { message: "name is required" })
  @MaxLength(MAX_NAME, {
    message: `name is longer than ${MAX_NAME} characters`,
  })
  name!: string;
}
