package {{ cookiecutter.java_package }}.service

import {{ cookiecutter.java_package }}.core.NotFoundException
import {{ cookiecutter.java_package }}.core.ValidationException
import {{ cookiecutter.java_package }}.dto.Item
import {{ cookiecutter.java_package }}.repository.ItemRepository
import org.springframework.stereotype.Service

const val MAX_NAME = 40

/** Business rules for items. Receives the repository; never touches HTTP. */
@Service
class ItemService(
    private val repository: ItemRepository,
) {
    fun list(): List<Item> = repository.list()

    fun get(id: Int): Item = repository.get(id) ?: throw NotFoundException("item $id not found")

    fun create(rawName: String?): Item {
        val name = rawName?.trim().orEmpty()
        if (name.isEmpty()) {
            throw ValidationException("name is required", "name")
        }
        if (name.length > MAX_NAME) {
            throw ValidationException("name is longer than $MAX_NAME characters", "name")
        }
        return repository.add(name)
    }
}
