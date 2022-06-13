import json
import os
import requests


def get(url):
    return requests.get(
        f"https://api.rytr.me/v1/{url}",
        headers={
            "Content-Type": "application/json",
            "Authentication": "Bearer " + os.environ["RYTR_API_KEY"],
        },
    ).json()


def post(url, data):
    return requests.post(
        f"https://api.rytr.me/v1/{url}",
        data=json.dumps(data),
        headers={
            "Content-Type": "application/json",
            "Authentication": "Bearer " + os.environ["RYTR_API_KEY"],
        },
    ).json()


def search_slug(data, slug):
    for item in data:
        if item["slug"] == slug:
            return item
    return None
