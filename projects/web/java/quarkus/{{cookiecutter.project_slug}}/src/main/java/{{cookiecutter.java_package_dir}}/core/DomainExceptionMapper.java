package {{ cookiecutter.java_package }}.core;

import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.ws.rs.ext.ExceptionMapper;
import jakarta.ws.rs.ext.Provider;
import java.util.LinkedHashMap;
import java.util.Map;

/** Turns a DomainException into {"detail": {"code", "message", "field"}}. */
@Provider
public class DomainExceptionMapper implements ExceptionMapper<DomainException> {
    @Override
    public Response toResponse(DomainException exception) {
        Map<String, Object> detail = new LinkedHashMap<>();
        detail.put("code", exception.code());
        detail.put("message", exception.getMessage());
        if (exception.field() != null) {
            detail.put("field", exception.field());
        }
        return Response.status(exception.status())
            .type(MediaType.APPLICATION_JSON)
            .entity(Map.of("detail", detail))
            .build();
    }
}
