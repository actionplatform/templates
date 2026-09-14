package {{ cookiecutter.java_package }}.service;

import {{ cookiecutter.java_package }}.core.NotFoundException;
import {{ cookiecutter.java_package }}.core.ValidationException;
import {{ cookiecutter.java_package }}.dto.Item;
import {{ cookiecutter.java_package }}.repository.ItemRepository;
import java.util.List;
import org.springframework.stereotype.Service;

/** Business rules for items. Receives the repository; never touches HTTP. */
@Service
public class ItemService {
    static final int MAX_NAME = 40;

    private final ItemRepository repository;

    public ItemService(ItemRepository repository) {
        this.repository = repository;
    }

    public List<Item> list() {
        return repository.list();
    }

    public Item get(int id) {
        return repository.get(id).orElseThrow(() -> new NotFoundException("item " + id + " not found"));
    }

    public Item create(String rawName) {
        String name = rawName == null ? "" : rawName.trim();
        if (name.isEmpty()) {
            throw new ValidationException("name is required", "name");
        }
        if (name.length() > MAX_NAME) {
            throw new ValidationException("name is longer than " + MAX_NAME + " characters", "name");
        }
        return repository.add(name);
    }
}
