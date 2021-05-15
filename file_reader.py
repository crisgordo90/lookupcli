import re


def fetch_ips(path="fixtures/list_of_ips.txt"):
    """
    Extract the list of IPs from the txt.file
    :return: list of ips
    """
    ip_pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
    with open(path, "r") as list_of_ips:
        fstring = list_of_ips.read()
        return re.findall(ip_pattern, fstring)
