package {{ cookiecutter.java_package }}.api

import {{ cookiecutter.java_package }}.Version
import {{ cookiecutter.java_package }}.dto.Health
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RestController

/** Ping. Every API exposes it at the root. */
@RestController
class PingController {
    @GetMapping("/ping")
    fun ping() = Health("ok", Version.VERSION)
}
