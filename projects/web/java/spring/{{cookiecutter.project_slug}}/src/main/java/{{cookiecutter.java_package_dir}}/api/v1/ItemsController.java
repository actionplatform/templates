package {{ cookiecutter.java_package }}.api.v1;

import {{ cookiecutter.java_package }}.dto.Item;
import {{ cookiecutter.java_package }}.dto.ItemCreate;
import {{ cookiecutter.java_package }}.service.ItemService;
import java.util.List;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

/** Example resource showing the layers: controller → service → repository. */
@RestController
@RequestMapping("/api/v1/items")
public class ItemsController {
    private final ItemService service;

    public ItemsController(ItemService service) {
        this.service = service;
    }

    @GetMapping
    public List<Item> list() {
        return service.list();
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public Item create(@RequestBody ItemCreate body) {
        return service.create(body.name());
    }

    @GetMapping("/{id}")
    public Item get(@PathVariable int id) {
        return service.get(id);
    }
}
