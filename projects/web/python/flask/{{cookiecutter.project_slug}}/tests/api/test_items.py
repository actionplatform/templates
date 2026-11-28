from app import create_app
from tests.support import make_client


def test_create_list_and_get():
    client = make_client()

    created = client.post("/api/v1/items", json={"name": "pen"})

    assert created.status_code == 201
    assert created.get_json()["name"] == "pen"

    id = created.get_json()["id"]

    assert created.get_json() in client.get("/api/v1/items").get_json()
    assert client.get(f"/api/v1/items/{id}").get_json() == created.get_json()


def test_each_app_has_its_own_store():
    first = create_app().test_client()
    second = create_app().test_client()

    first.post("/api/v1/items", json={"name": "pen"})

    assert len(first.get("/api/v1/items").get_json()) == 1
    assert second.get("/api/v1/items").get_json() == []


def test_errors_have_one_shape():
    client = make_client()

    blank = client.post("/api/v1/items", json={"name": "  "})
    wrong_type = client.post("/api/v1/items", json={"name": 7})
    not_object = client.post("/api/v1/items", json=["pen"])
    not_json = client.post(
        "/api/v1/items", data="{", content_type="text/plain"
    )
    unknown = client.get("/api/v1/items/999999")

    assert blank.status_code == 422
    assert blank.get_json() == {
        "detail": {
            "code": "invalid",
            "message": "name is required",
            "field": "name",
        }
    }
    assert wrong_type.status_code == 422
    assert wrong_type.get_json()["detail"]["field"] == "name"
    assert not_object.status_code == 422
    assert "field" not in not_object.get_json()["detail"]
    assert not_json.status_code == 422
    assert unknown.status_code == 404
    assert unknown.get_json() == {
        "detail": {"code": "not_found", "message": "item 999999 not found"}
    }


def test_unknown_route_and_method_use_the_same_shape():
    client = make_client()

    route = client.get("/nope")
    method = client.delete("/api/v1/items")

    assert route.status_code == 404
    assert route.get_json()["detail"]["code"] == "not_found"
    assert method.status_code == 405
    assert method.get_json()["detail"]["code"] == "method_not_allowed"
