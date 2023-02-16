import json
import requests

# API documentation: https://swagger-api-support.lambdatest.com/index.html#/Build

username = "your lambdatest username"
access_token = "your lambdatest access token"

def test_get_lambdatest_all_builds():
    url = "https://%s:%s@api.lambdatest.com/automation/api/v1/builds" % (username, access_token)
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    
def test_update_lambdatest_build_name():
    url = "https://%s:%s@api.lambdatest.com/automation/api/v1/builds/10391473" % (username, access_token)
    headers = {"accept": "application/json", "Content-Type": "application/json"}
    payload = {
        "name": "My build name"
    }
    response = requests.patch(url, headers=headers, data=json.dumps(payload))
    assert response.status_code == 200

def test_get_lambdatest_build():
    url = "https://%s:%s@api.lambdatest.com/automation/api/v1/builds/10391473" % (username, access_token)
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200

def test_delete_lambdatest_build():
    url = "https://%s:%s@api.lambdatest.com/automation/api/v1/builds/5539501" % (username, access_token)
    headers = {"accept": "application/json"}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 200