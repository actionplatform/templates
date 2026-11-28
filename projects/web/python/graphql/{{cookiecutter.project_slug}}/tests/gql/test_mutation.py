from tests.support import graphql, make_client

CREATE = "mutation($n: String!) { createItem(input: {name: $n}) { id name } }"


def test_create_item_trims_the_name():
    body = graphql(make_client(), CREATE, {"n": " ink "})

    assert body["data"]["createItem"]["name"] == "ink"
    assert "errors" not in body


def test_invalid_name_carries_code_and_field():
    body = graphql(make_client(), CREATE, {"n": "  "})

    assert body["data"] is None
    assert body["errors"][0]["message"] == "name is required"
    assert body["errors"][0]["extensions"] == {
        "code": "invalid",
        "field": "name",
    }
