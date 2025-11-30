def test_update_project_positive(api, new_project):
    project_id = new_project
    payload = {"title": "UpdatedName"}

    response = api.update_project(project_id, payload)
    print(response.json())

    assert response.status_code == 200


def test_update_project_negative_wrong_id(api):
    payload = {"title": "NewName"}

    response = api.update_project("wrong-id-123", payload)
    print(response.json())

    assert response.status_code == 404
