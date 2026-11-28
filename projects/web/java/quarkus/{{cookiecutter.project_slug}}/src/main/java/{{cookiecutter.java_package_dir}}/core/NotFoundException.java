package {{ cookiecutter.java_package }}.core;

public class NotFoundException extends DomainException {
    public NotFoundException(String message) {
        super(404, "not_found", message, null);
    }
}
