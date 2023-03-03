# -*- coding: utf-8 -*-

import bleach
import requests
import logging

logger = logging.getLogger(__name__)

api_endpoint = "http://localhost:8080/api"


class ApiConnectionError(Exception):
    def __init__(self, status_code):
        self.msg = f"The response received a status code: {status_code}"

    def __str__(self):
        return self.msg


def send_request(method, url, data=None):
    match method:
        case "GET":
            response = requests.get(url=url)
        case "POST":
            response = requests.post(url=url, data=data)
        case "DELETE":
            response = requests.delete(url=url)
        case _:
            raise Exception
    if response.status_code != 200:
        raise ApiConnectionError(status_code=response.status_code)
    logger.info(f"Response: {response.json()}")
    return response.json()


def add(text):
    sanitize_text = bleach.clean(text=text)
    return send_request(
        method="POST", url=f"{api_endpoint}/todos", data={"text": sanitize_text}
    )


def delete(todo_id):
    if find(todo_id):
        send_request("DELETE", f"{api_endpoint}/todos/{todo_id}")
        return True
    else:
        return False


def get_all():
    return send_request("GET", f"{api_endpoint}/todos")


def find(todo_id):
    result = False
    for element in get_all():
        if element.get("_id") == todo_id:
            result = True
    return result
