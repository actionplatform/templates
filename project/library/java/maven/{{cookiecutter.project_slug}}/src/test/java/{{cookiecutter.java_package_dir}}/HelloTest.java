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
    void versionIsSet() {
        assertEquals("0.1.0", Version.VERSION);
    }
}
