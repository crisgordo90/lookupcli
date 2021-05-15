from request_handler import RequestHandler

GEO_IP_LOOKUP_ENDPOINT = "http://ipwhois.app/json"


def perform_geo_ip_lookup(ips: list, sample: int) -> dict:
    """
    Perform a RDAP lookup on the given ips
    :param ips: list of ips
    :param sample: Using a sample since the endpoint only allows a certain amount of request
    :return: a dictionary of the results
    """
    lookups = {}
    for ip in ips[:sample]:
        response = RequestHandler().lookup_info(GEO_IP_LOOKUP_ENDPOINT, ip)
        lookups[ip] = response

    return lookups
