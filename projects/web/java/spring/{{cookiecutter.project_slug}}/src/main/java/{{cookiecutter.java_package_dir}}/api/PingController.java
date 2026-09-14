package {{ cookiecutter.java_package }}.api;

import {{ cookiecutter.java_package }}.Version;
import {{ cookiecutter.java_package }}.dto.Health;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/** Ping. Every API exposes it at the root. */
@RestController
public class PingController {
    @GetMapping("/ping")
    public Health ping() {
        return new Health("ok", Version.VERSION);
    }
}
