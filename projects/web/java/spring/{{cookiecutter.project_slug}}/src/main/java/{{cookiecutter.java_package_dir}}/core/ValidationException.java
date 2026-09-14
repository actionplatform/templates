package {{ cookiecutter.java_package }}.core;

import org.springframework.http.HttpStatus;

public class ValidationException extends DomainException {
    public ValidationException(String message, String field) {
        super(HttpStatus.UNPROCESSABLE_ENTITY, "invalid", message, field);
    }
}
