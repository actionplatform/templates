package {{ cookiecutter.java_package }}.core;

public class ValidationException extends DomainException {
    public ValidationException(String message, String field) {
        super(422, "invalid", message, field);
    }
}
