package {{ cookiecutter.java_package }}.core;

import java.util.LinkedHashMap;
import java.util.Map;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

/** Turns a DomainException into {"detail": {"code", "message", "field"}}. */
@RestControllerAdvice
public class ApiExceptionHandler {
    @ExceptionHandler(DomainException.class)
    public ResponseEntity<Map<String, Object>> domain(DomainException exception) {
        Map<String, Object> detail = new LinkedHashMap<>();
        detail.put("code", exception.code());
        detail.put("message", exception.getMessage());
        if (exception.field() != null) {
            detail.put("field", exception.field());
        }
        return ResponseEntity.status(exception.status()).body(Map.of("detail", detail));
    }
}
