#!/usr/bin/python

import sys
import getopt
import geo_ip_lookup
import rdap_lookup
import file_reader

VERSION = "0.0.1"
FACTOR = 1
USAGE = """
LookupsCLI is a tool to run ip lookups
Using a sample of 50 since the endpoint only allows a certain amount of request
-g         # Performs a RDAP lookup on the list_of_ips
-r         # Performs a Geo IP lookup on the list_of_ips  

"""


def entrypoint():
    options, arguments = getopt.getopt(sys.argv[1:], "vhgr", ["version", "help", "geo", "rdap"])
    separator = "\n"

    list_of_ips = file_reader.fetch_ips()
    for o, a in options:
        if o in ("-g", "--geo"):
            print(geo_ip_lookup.perform_geo_ip_lookup(list_of_ips, 5 * FACTOR))
        if o in ("-r", "--rdap"):
            print(rdap_lookup.perform_rdap_lookup(list_of_ips, 5 * FACTOR))
        if o in ("-v", "--version"):
            print(VERSION)
            sys.exit()
        if o in ("-h", "--help"):
            print(USAGE)
            sys.exit()
        if o in ("-s", "--separator"):
            separator = a
    if not arguments or len(arguments) > 3:
        raise SystemExit(USAGE)
    try:
        operands = [int(arg) for arg in arguments]
    except ValueError:
        raise SystemExit(USAGE)
    return separator, operands


if __name__ == "__main__":
    entrypoint()
