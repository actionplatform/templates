package {{ cookiecutter.java_package }}.core;

import org.springframework.http.HttpStatus;

public class ConflictException extends DomainException {
    public ConflictException(String message) {
        super(HttpStatus.CONFLICT, "conflict", message, null);
    }
}
