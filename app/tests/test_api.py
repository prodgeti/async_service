import uuid


def test_ping(client):
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"status": "Server is running"}


def test_create_and_retrieve_query(client):
    """Tests creating a record and retrieving it by cadastral number."""
    unique_cadastral_number = str(uuid.uuid4())
    query_data = {
        "cadastral_number": unique_cadastral_number,
        "latitude": 55.7558,
        "longitude": 37.6173
    }

    response = client.post("/query", json=query_data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["result"] in [True, False]

    cadastral_number = query_data["cadastral_number"]
    response = client.get(f"/history/{cadastral_number}")
    assert response.status_code == 200
    history_data = response.json()
    assert len(history_data) > 0
    assert history_data[0]["cadastral_number"] == query_data["cadastral_number"]

    response = client.post("/query", json=query_data)
    assert response.status_code == 400
    error_data = response.json()
    assert "detail" in error_data
    assert error_data["detail"] == "Запись с таким кадастровым номером уже существует."


def test_history(client):
    response = client.get("/history")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_result(client):
    response = client.get("/result")
    assert response.status_code == 200
    assert "result" in response.json()
