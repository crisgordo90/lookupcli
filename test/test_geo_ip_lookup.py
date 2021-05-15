import pytest
import requests_mock
import geo_ip_lookup


@pytest.fixture()
def response():
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


def test_lookup_info(response):
    ip = "8.8.4.4"
    with requests_mock.Mocker() as m:
        m.get("http://ipwhois.app/json/8.8.4.4", json=response)
        result = geo_ip_lookup.perform_geo_ip_lookup([ip], 1)
        assert {ip: response} == result

