package {{ cookiecutter.java_package }}.core;

/** A rule violation the caller can act on. Services throw it; the API answers it in one shape. */
public class DomainException extends RuntimeException {
    private final int status;
    private final String code;
    private final String field;

    public DomainException(int status, String code, String message, String field) {
        super(message);
        this.status = status;
        this.code = code;
        this.field = field;
    }

    public int status() {
        return status;
    }

    public String code() {
        return code;
    }

    public String field() {
        return field;
    }
}
