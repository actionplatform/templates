package {{ cookiecutter.java_package }};

/** Dummy public class. Replace with the real API. */
public final class Hello {
    private Hello() {
    }

    public static String greet(String name) {
        return "hello, " + (name == null || name.isEmpty() ? "world" : name);
    }
}
