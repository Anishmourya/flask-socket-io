"""Socket Test"""


def test_socket(client):
    res = client.get("/")
    assert res.status_code == 200
