import re

from api_testing.api.httpbin_api import http_bin_api
from http import HTTPStatus


def test_list_html():
    res = http_bin_api.list_html()
    assert res.status_code == HTTPStatus.OK
    # checking header
    assert res.headers["Content-Type"] == "text/html; charset=utf-8"


def test_image_jpeg():
    res = http_bin_api.image_jpeg()
    assert res.status_code == HTTPStatus.OK
    assert res.headers["Content-Type"] == "image/jpeg"


def test_robots():
    res = http_bin_api.robots_txt()
    assert res.status_code == HTTPStatus.OK
    assert res.headers["Content-Type"] == "text/plain"
    # in the ody of response there are these two expressions anywhere
    assert re.fullmatch(r".*User-agent: \*.*Disallow: /deny.*", res.text,
                        flags=re.DOTALL)
