from tests.support import make_client


def test_create_list_and_get():
    client = make_client()

    created = client.post("/api/v1/items", {"name": "pen"}, format="json")

    assert created.status_code == 201
    assert created.json()["name"] == "pen"

    id = created.json()["id"]

    assert created.json() in client.get("/api/v1/items").json()
    assert client.get(f"/api/v1/items/{id}").json() == created.json()


def test_errors_have_one_shape():
    client = make_client()

    blank = client.post("/api/v1/items", {"name": "  "}, format="json")
    missing_field = client.post("/api/v1/items", {}, format="json")
    unknown = client.get("/api/v1/items/999999")

    assert blank.status_code == 422
    assert blank.json() == {
        "detail": {
            "code": "invalid",
            "message": "name is required",
            "field": "name",
        }
    }
    assert missing_field.status_code == 422
    assert missing_field.json()["detail"]["code"] == "invalid"
    assert missing_field.json()["detail"]["field"] == "name"
    assert unknown.status_code == 404
    assert unknown.json() == {
        "detail": {"code": "not_found", "message": "item 999999 not found"}
    }


def test_unknown_route_and_method_use_the_same_shape():
    client = make_client()

    route = client.get("/nope")
    method = client.delete("/api/v1/items")

    assert route.status_code == 404
    assert route.json()["detail"]["code"] == "not_found"
    assert method.status_code == 405
    assert method.json()["detail"]["code"] == "method_not_allowed"


def test_malformed_json_is_refused():
    response = make_client().post(
        "/api/v1/items", "{", content_type="application/json"
    )

    assert response.status_code == 400
    assert response.json()["detail"]["code"] == "parse_error"
