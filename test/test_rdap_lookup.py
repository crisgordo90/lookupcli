import pytest
import requests_mock
import rdap_lookup


@pytest.fixture()
def response():
    return {
        "rdapConformance": ["rdap_level_0", "cidr0", "arin_originas0"],
        "notices": [{
            "title": "Terms of Service",
            "description": ["By using the ARIN RDAP/Whois service, you are agreeing to the RDAP/Whois Terms of Use"],
            "links": [{
                "value": "https://rdap.arin.net/registry/ip/8.8.4.4/24",
                "rel": "about",
                "type": "text/html",
                "href": "https://www.arin.net/resources/registry/whois/tou/"
            }]
        }, {
            "title": "Whois Inaccuracy Reporting",
            "description": ["If you see inaccuracies in the results, please visit: "],
            "links": [{
                "value": "https://rdap.arin.net/registry/ip/8.8.4.4/24",
                "rel": "about",
                "type": "text/html",
                "href": "https://www.arin.net/resources/registry/whois/inaccuracy_reporting/"
            }]
        }, {
            "title": "Copyright Notice",
            "description": ["Copyright 1997-2021, American Registry for Internet Numbers, Ltd."]
        }],
        "handle": "NET-8-8-4-0-1",
        "startAddress": "8.8.4.0",
        "endAddress": "8.8.4.255",
        "ipVersion": "v4",
        "name": "LVLT-GOGL-8-8-4",
        "type": "ALLOCATION",
        "parentHandle": "NET-8-0-0-0-1",
        "events": [{
            "eventAction": "last changed",
            "eventDate": "2014-03-14T16:52:03-04:00"
        }, {
            "eventAction": "registration",
            "eventDate": "2014-03-14T16:52:03-04:00"
        }],
        "links": [{
            "value": "https://rdap.arin.net/registry/ip/8.8.4.4/24",
            "rel": "self",
            "type": "application/rdap+json",
            "href": "https://rdap.arin.net/registry/ip/8.8.4.0"
        }, {
            "value": "https://rdap.arin.net/registry/ip/8.8.4.4/24",
            "rel": "alternate",
            "type": "application/xml",
            "href": "https://whois.arin.net/rest/net/NET-8-8-4-0-1"
        }, {
            "value": "https://rdap.arin.net/registry/ip/8.8.4.4/24",
            "rel": "up",
            "type": "application/rdap+json",
            "href": "https://rdap.arin.net/registry/ip/8.0.0.0/9"
        }],
        "entities": [{
            "handle": "GOGL",
            "vcardArray": ["vcard", [["version", {}, "text", "4.0"], ["fn", {}, "text", "Google LLC"], ["adr", {
                "label": "1600 Amphitheatre Parkway\nMountain View\nCA\n94043\nUnited States"
            }, "text", ["", "", "", "", "", "", ""]], ["kind", {}, "text", "org"]]],
            "roles": ["registrant"],
            "remarks": [{
                "title": "Registration Comments",
                "description": [
                    "Please note that the recommended way to file abuse complaints are located in the following links. ",
                    "", "To report abuse and illegal activity: https://www.google.com/contact/", "",
                    "For legal requests: http://support.google.com/legal ", "", "Regards, ", "The Google Team"]
            }],
            "links": [{
                "value": "https://rdap.arin.net/registry/ip/8.8.4.4/24",
                "rel": "self",
                "type": "application/rdap+json",
                "href": "https://rdap.arin.net/registry/entity/GOGL"
            }, {
                "value": "https://rdap.arin.net/registry/ip/8.8.4.4/24",
                "rel": "alternate",
                "type": "application/xml",
                "href": "https://whois.arin.net/rest/org/GOGL"
            }],
            "events": [{
                "eventAction": "last changed",
                "eventDate": "2019-10-31T15:45:45-04:00"
            }, {
                "eventAction": "registration",
                "eventDate": "2000-03-30T00:00:00-05:00"
            }],
            "entities": [{
                "handle": "ABUSE5250-ARIN",
                "vcardArray": ["vcard", [["version", {}, "text", "4.0"], ["adr", {
                    "label": "1600 Amphitheatre Parkway\nMountain View\nCA\n94043\nUnited States"
                }, "text", ["", "", "", "", "", "", ""]], ["fn", {}, "text", "Abuse"], ["org", {}, "text", "Abuse"],
                                         ["kind", {}, "text", "group"],
                                         ["email", {}, "text", "network-abuse@google.com"], ["tel", {
                        "type": ["work", "voice"]
                    }, "text", "+1-650-253-0000"]]],
                "roles": ["abuse"],
                "remarks": [{
                    "title": "Registration Comments",
                    "description": [
                        "Please note that the recommended way to file abuse complaints are located in the following links.",
                        "", "To report abuse and illegal activity: https://www.google.com/contact/", "",
                        "For legal requests: http://support.google.com/legal ", "", "Regards,", "The Google Team"]
                }, {
                    "title": "Unvalidated POC",
                    "description": [
                        "ARIN has attempted to validate the data for this POC, but has received no response from the POC since 2019-10-24"]
                }],
                "links": [{
                    "value": "https://rdap.arin.net/registry/ip/8.8.4.4/24",
                    "rel": "self",
                    "type": "application/rdap+json",
                    "href": "https://rdap.arin.net/registry/entity/ABUSE5250-ARIN"
                }, {
                    "value": "https://rdap.arin.net/registry/ip/8.8.4.4/24",
                    "rel": "alternate",
                    "type": "application/xml",
                    "href": "https://whois.arin.net/rest/poc/ABUSE5250-ARIN"
                }],
                "events": [{
                    "eventAction": "last changed",
                    "eventDate": "2018-10-24T11:23:55-04:00"
                }, {
                    "eventAction": "registration",
                    "eventDate": "2015-11-06T15:36:35-05:00"
                }],
                "port43": "whois.arin.net",
                "objectClassName": "entity"
            }, {
                "handle": "ZG39-ARIN",
                "vcardArray": ["vcard", [["version", {}, "text", "4.0"], ["adr", {
                    "label": "1600 Amphitheatre Parkway\nMountain View\nCA\n94043\nUnited States"
                }, "text", ["", "", "", "", "", "", ""]], ["fn", {}, "text", "Google LLC"],
                                         ["org", {}, "text", "Google LLC"], ["kind", {}, "text", "group"],
                                         ["email", {}, "text", "arin-contact@google.com"], ["tel", {
                        "type": ["work", "voice"]
                    }, "text", "+1-650-253-0000"]]],
                "roles": ["technical", "administrative"],
                "links": [{
                    "value": "https://rdap.arin.net/registry/ip/8.8.4.4/24",
                    "rel": "self",
                    "type": "application/rdap+json",
                    "href": "https://rdap.arin.net/registry/entity/ZG39-ARIN"
                }, {
                    "value": "https://rdap.arin.net/registry/ip/8.8.4.4/24",
                    "rel": "alternate",
                    "type": "application/xml",
                    "href": "https://whois.arin.net/rest/poc/ZG39-ARIN"
                }],
                "events": [{
                    "eventAction": "last changed",
                    "eventDate": "2019-10-30T07:05:21-04:00"
                }, {
                    "eventAction": "registration",
                    "eventDate": "2000-11-30T13:54:08-05:00"
                }],
                "status": ["validated"],
                "port43": "whois.arin.net",
                "objectClassName": "entity"
            }],
            "port43": "whois.arin.net",
            "objectClassName": "entity"
        }],
        "port43": "whois.arin.net",
        "status": ["active"],
        "objectClassName": "ip network",
        "cidr0_cidrs": [{
            "v4prefix": "8.8.4.0",
            "length": 24
        }],
        "arin_originas0_originautnums": []
    }


def test_lookup_info(response):
    ip = "8.8.4.4"
    with requests_mock.Mocker() as m:
        m.get("https://rdap.arin.net/registry/ip/8.8.4.4/24", json=response)
        result = rdap_lookup.perform_rdap_lookup([ip], 1)
        assert {ip: response} == result