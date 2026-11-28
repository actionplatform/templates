package {{ cookiecutter.java_package }}.service;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import {{ cookiecutter.java_package }}.core.NotFoundException;
import {{ cookiecutter.java_package }}.core.ValidationException;
import {{ cookiecutter.java_package }}.dto.Item;
import {{ cookiecutter.java_package }}.repository.ItemRepository;
import org.junit.jupiter.api.Test;

class ItemServiceTest {
    private final ItemService service = new ItemService(new ItemRepository());

    @Test
    void createsAndGetsWithoutHttp() {
        Item item = service.create(" pen ");
        assertEquals("pen", item.name());
        assertEquals(item, service.get(item.id()));
        assertEquals(1, service.list().size());
    }

    @Test
    void refusesBadNamesAndUnknownIds() {
        assertThrows(ValidationException.class, () -> service.create(""));
        assertThrows(ValidationException.class, () -> service.create("x".repeat(41)));
        assertThrows(NotFoundException.class, () -> service.get(1));
    }
}
