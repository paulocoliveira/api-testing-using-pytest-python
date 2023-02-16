import requests

# API documentation: https://reqres.in/

def test_get_list_of_users():
    url = "https://reqres.in/api/users"
    response = requests.get(url)
    assert response.status_code == 200
    
def test_create_new_user():
    url = "https://reqres.in/api/users"
    data = {
        "name": "Paulo Oliveira",
        "movies": ["I Love You Man", "Role Models"]
    }
    response = requests.post(url, data=data)
    assert response.status_code == 201

def test_update_user():
    url = "https://reqres.in/api/users/2"
    data = {
        "name": "Paulo Updated"
    }
    response = requests.put(url, data=data)
    assert response.status_code == 200

def test_delete_user():
    url = "https://reqres.in/api/users/2"
    response = requests.delete(url)
    assert response.status_code == 204
