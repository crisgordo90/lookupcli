import pytest
import requests_mock
import request_handler


@pytest.fixture()
def response_google():
    return {
        "ip": "8.8.4.4",
        "success": True,
        "type": "IPv4",
        "continent": "North America",
        "continent_code": "NA",
        "country": "United States",
        "country_code": "US",
        "country_flag": "https://cdn.ipwhois.io/flags/us.svg",
        "country_capital": "Washington",
        "country_phone": "+1",
        "country_neighbours": "CA,MX,CU",
        "region": "California",
        "city": "Mountain View",
        "latitude": 37.3860517,
        "longitude": -122.0838511,
        "asn": "AS15169",
        "org": "Google LLC",
        "isp": "Google LLC",
        "timezone": "America/Los_Angeles",
        "timezone_name": "Pacific Standard Time",
        "timezone_dstOffset": 0,
        "timezone_gmtOffset": -28800,
        "timezone_gmt": "GMT -8:00",
        "currency": "US Dollar",
        "currency_code": "USD",
        "currency_symbol": "$",
        "currency_rates": 1,
        "currency_plural": "US dollars",
        "completed_requests": 9
    }


@pytest.fixture()
def rh():
    return request_handler.RequestHandler()


def test_lookup_info(rh, response_google):
    with requests_mock.Mocker() as m:
        m.get("http://ipwhois.app/json/8.8.4.4", json=response_google)
        result = rh.lookup_info("http://ipwhois.app/json", "8.8.4.4")
        assert result == response_google


def test_log_and_sleep(rh, response_google):
    with requests_mock.Mocker() as m:
        m.get("http://ipwhois.app/json/8.8.4.4", json=response_google)
        # result = rh.log_and_sleep("wip", "wip")
        # assert result == "wip"
