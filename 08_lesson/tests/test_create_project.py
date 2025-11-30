def test_create_project_positive(api):
    payload = {
        "title": "MyTestProject",
        "users": {
            "user_id": "admin"
        }
    }
    response = api.create_project(payload)
    print(response.json())
    assert response.status_code == 201


def test_create_project_negative_no_title(api):
    payload = {
        "users": {
            "user_id": "admin"
        }
    }
    response = api.create_project(payload)
    print(response.json())
    assert response.status_code == 400
