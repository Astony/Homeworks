from collections import Counter

import requests

"""
Function get some url, check that the url exists
and then read the content of url. In case when url doesn't exist
function's raise ValueError
"""


def count_i_chars(url: str) -> int:
    web_url = requests.get(url)
    if web_url.status_code != 200:
        raise ValueError("Unreachable {url}")
    counter = Counter(web_url.text)
    return counter["i"]
