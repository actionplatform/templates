package {{ cookiecutter.java_package }}.repository;

import {{ cookiecutter.java_package }}.dto.Item;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import org.springframework.stereotype.Repository;

/** In-memory store standing in for a database or an external API. Replace it; keep the methods. */
@Repository
public class ItemRepository {
    private final Map<Integer, Item> rows = new LinkedHashMap<>();
    private int lastId = 0;

    public synchronized List<Item> list() {
        return new ArrayList<>(rows.values());
    }

    public synchronized Optional<Item> get(int id) {
        return Optional.ofNullable(rows.get(id));
    }

    public synchronized Item add(String name) {
        lastId += 1;
        Item item = new Item(lastId, name);
        rows.put(item.id(), item);
        return item;
    }
}
