package {{ cookiecutter.java_package }}.api.v1;

import {{ cookiecutter.java_package }}.dto.Item;
import {{ cookiecutter.java_package }}.dto.ItemCreate;
import {{ cookiecutter.java_package }}.service.ItemService;
import jakarta.inject.Inject;
import jakarta.ws.rs.Consumes;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.POST;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.PathParam;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.util.List;

/** Example resource showing the layers: resource → service → repository. */
@Path("/api/v1/items")
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
public class ItemsResource {
    private final ItemService service;

    @Inject
    public ItemsResource(ItemService service) {
        this.service = service;
    }

    @GET
    public List<Item> list() {
        return service.list();
    }

    @POST
    public Response create(ItemCreate body) {
        Item item = service.create(body == null ? null : body.name());
        return Response.status(Response.Status.CREATED).entity(item).build();
    }

    @GET
    @Path("/{id}")
    public Item get(@PathParam("id") int id) {
        return service.get(id);
    }
}
