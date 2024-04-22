import os
import requests


class Common:

    def Send_request(request, paramaters) -> dict:
        response = requests.get(request, params=paramaters)
        while response.status_code != 200:
            if response.status_code == 404:
                break
            response = requests.get(request, params=paramaters)
        return response.json()

    def Verify_path(path) -> None:
        if not os.path.exists(path):
            os.makedirs(path)
    
    def Verify_string(text) -> str:
        if type(text) == str:
            for char in "\/*":
                text = text.replace(char, "")
            return text