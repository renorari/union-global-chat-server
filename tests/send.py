import requests

token = "F53HyHtNaP3e7n29yCGWleiw0cGsH7dm"

def request(method: str, url: str, *args, **kwargs):
    kwargs["headers"] = {"Authorization": "Bearer {}".format(token)}
    return requests.request(method, "http://localhost:8080/api/v1" + url, *args, **kwargs)


def send():
    request("POST", "/channels", json={"test": "test"})

send()