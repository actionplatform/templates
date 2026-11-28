from tests.support import graphql, make_client

CREATE = "mutation($n: String!) { createItem(input: {name: $n}) { id name } }"


def test_list_and_get():
    client = make_client()
    created = graphql(client, CREATE, {"n": "pen"})["data"]["createItem"]

    listed = graphql(client, "{ items { id name } }")["data"]["items"]
    fetched = graphql(
        client,
        "query($id: Int!) { item(id: $id) { id name } }",
        {"id": created["id"]},
    )["data"]["item"]

    assert created in listed
    assert fetched == created


def test_unknown_item_is_a_not_found_error():
    body = graphql(make_client(), "{ item(id: 999999) { id } }")

    assert body["data"] is None
    assert body["errors"][0]["extensions"] == {
        "code": "not_found",
        "field": None,
    }
