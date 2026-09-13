package {{ cookiecutter.java_package }};

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class HelloTest {
    @Test
    void defaultsToWorld() {
        assertEquals("hello, world", Hello.greet(""));
    }

    @Test
    void greetsName() {
        assertEquals("hello, ana", Hello.greet("ana"));
    }

    @Test
    void versionMatchesLastVersion() throws java.io.IOException {
        String expected = java.nio.file.Files.readString(java.nio.file.Path.of("LAST_VERSION")).trim();
        assertEquals(expected, Version.VERSION);
    }
}
