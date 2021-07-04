from unittest.mock import patch

import pytest

from homework4.task02.url_func import count_i_chars

"""Create fake url and set it's content and status code"""


def test_count_every_i_in_existing_fake_url():
    with patch("requests.get") as mock_request:
        url = "https://fakeURL.com/"
        mock_request.return_value.text = "The number of i = 3\nii"
        mock_request.return_value.status_code = 200
        assert count_i_chars(url) == 3


def test_ValueError_output_in_non_existing_fake_url():
    with patch("requests.get") as mock_request:
        url = "https://fakeURL.com/"
        mock_request.return_value.text = "The number of i = 3\nii"
        mock_request.return_value.status_code = 404
        with pytest.raises(ValueError):
            count_i_chars(url)
