import requests

"""
Function get some url, check that the url exists
and then read the content of url. In case when url doesn't exist
function's raise ValueError
"""


def count_i_chars(url: str) -> int:
    web_url = requests.get(url)
    if web_url.status_code == 200:
        counter = 0
        for char in web_url.text:
            if char == "i":
                counter += 1
        return counter
    else:
        raise ValueError("Unreachable {url}")
