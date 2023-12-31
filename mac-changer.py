#!/usr/bin/env python
import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option(
        "-i",
        "--interface",
        dest="interface",
        help="Interface to change the MAC address.",
    )
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")

    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")
    return options


def change_mac(interface, new_mac):
    print("Changing the {} to address {}".format(interface, new_mac))
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])

    mac_address_search_result = re.search(
        r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result
    ).group()

    if mac_address_search_result:
        return mac_address_search_result
    else:
        print("Error, Could not find valid MAC Address")


options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC = {}").format(current_mac)
# change_mac(options.interface, options.new_mac)
