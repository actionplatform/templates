package {{ cookiecutter.java_package }}.api;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.hasItem;
import static org.hamcrest.Matchers.notNullValue;

import {{ cookiecutter.java_package }}.Version;
import io.quarkus.test.junit.QuarkusTest;
import io.restassured.http.ContentType;
import org.junit.jupiter.api.Test;

@QuarkusTest
class ApiTest {
    private int createItem(String name) {
        return given()
            .contentType(ContentType.JSON)
            .body("{\"name\": \"" + name + "\"}")
            .when().post("/api/v1/items")
            .then().statusCode(201).body("name", equalTo(name)).body("id", notNullValue())
            .extract().path("id");
    }

    @Test
    void health() {
        given().when().get("/health")
            .then().statusCode(200).contentType(ContentType.JSON)
            .body("status", equalTo("ok"))
            .body("version", equalTo(Version.VERSION));
    }

    @Test
    void createsListsAndGetsItems() {
        int id = createItem("pen");
        given().when().get("/api/v1/items").then().statusCode(200).body("id", hasItem(id));
        given().when().get("/api/v1/items/" + id).then().statusCode(200)
            .body("id", equalTo(id))
            .body("name", equalTo("pen"));
    }

    @Test
    void errorsHaveOneShape() {
        given().contentType(ContentType.JSON).body("{\"name\": \"  \"}")
            .when().post("/api/v1/items")
            .then().statusCode(422)
            .body("detail.code", equalTo("invalid"))
            .body("detail.field", equalTo("name"));
        given().contentType(ContentType.JSON).body("{}")
            .when().post("/api/v1/items")
            .then().statusCode(422)
            .body("detail.code", equalTo("invalid"));
        given().when().get("/api/v1/items/999999")
            .then().statusCode(404)
            .body("detail.code", equalTo("not_found"));
    }
}
