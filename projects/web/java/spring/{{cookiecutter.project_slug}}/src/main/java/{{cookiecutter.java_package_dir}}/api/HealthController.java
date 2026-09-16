package {{ cookiecutter.java_package }}.api;

import {{ cookiecutter.java_package }}.Version;
import {{ cookiecutter.java_package }}.dto.Health;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/** Health. Every API exposes it at the root. */
@RestController
public class HealthController {
    @GetMapping("/health")
    public Health health() {
        return new Health("ok", Version.VERSION);
    }
}
