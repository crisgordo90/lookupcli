from request_handler import RequestHandler

RDAP_LOOKUP_ENDPOINT = "https://rdap.arin.net/registry/ip"


def perform_rdap_lookup(ips: list, sample: int) -> dict:
    """
    Perform a RDAP lookup on the given ips
    :param ips: List of ips
    :param sample: Using a sample since the endpoint only allows a certain amount of request
    :return: A dictionary of the results
    """
    lookups = {}
    for ip in ips[:sample]:
        response = RequestHandler().lookup_info(RDAP_LOOKUP_ENDPOINT, f"{ip}/24")
        lookups[ip] = response

    return lookups
