package {{ cookiecutter.java_package }}.api;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import {{ cookiecutter.java_package }}.Version;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

@SpringBootTest
@AutoConfigureMockMvc
class ApiTest {
    @Autowired
    private MockMvc mvc;

    @Test
    void ping() throws Exception {
        mvc.perform(get("/ping"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.status").value("ok"))
            .andExpect(jsonPath("$.version").value(Version.VERSION));
    }

    @Test
    void createsListsAndGetsItems() throws Exception {
        mvc.perform(post("/api/v1/items").contentType(MediaType.APPLICATION_JSON).content("{\"name\": \"pen\"}"))
            .andExpect(status().isCreated())
            .andExpect(jsonPath("$.name").value("pen"));
        mvc.perform(get("/api/v1/items")).andExpect(status().isOk()).andExpect(jsonPath("$[0].name").value("pen"));
        mvc.perform(get("/api/v1/items/1")).andExpect(status().isOk()).andExpect(jsonPath("$.id").value(1));
    }

    @Test
    void errorsHaveOneShape() throws Exception {
        mvc.perform(post("/api/v1/items").contentType(MediaType.APPLICATION_JSON).content("{\"name\": \"  \"}"))
            .andExpect(status().isUnprocessableEntity())
            .andExpect(jsonPath("$.detail.code").value("invalid"))
            .andExpect(jsonPath("$.detail.field").value("name"));
        mvc.perform(get("/api/v1/items/999"))
            .andExpect(status().isNotFound())
            .andExpect(jsonPath("$.detail.code").value("not_found"));
    }
}
