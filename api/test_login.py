import json

import requests


def test_json():

    r = requests.post(
        "http://3r5z779982.wicp.vip:7000/api/authenticate",
        data=json.dumps({
            "username": "18858104920",
            "password": "123456",
            "rememberMe": "true"

        }),
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json"

        }

    )

    print(r.status_code)