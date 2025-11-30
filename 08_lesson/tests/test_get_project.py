def test_get_project_positive(api, new_project):
    project_id = new_project

    response = api.get_project(project_id)
    print(response.json())

    assert response.status_code == 200
    assert response.json()["id"] == project_id


def test_get_project_negative_not_found(api):
    response = api.get_project("non-existent-id-12345")
    print(response.json())

    assert response.status_code == 404
