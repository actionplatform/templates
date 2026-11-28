package {{ cookiecutter.java_package }}.api;

import {{ cookiecutter.java_package }}.Version;
import {{ cookiecutter.java_package }}.dto.Health;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;

/** Health. Every API exposes it at the root. */
@Path("/health")
@Produces(MediaType.APPLICATION_JSON)
public class HealthResource {
    @GET
    public Health health() {
        return new Health("ok", Version.VERSION);
    }
}
