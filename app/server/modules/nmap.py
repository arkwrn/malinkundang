#! /usr/bin/python3
# Maintainer : Arie Kurniawan - hubungi.aja@gmail.com
# January 2021

import nmap3
import json

def port_scanner(target):
    nmap = nmap3.Nmap()
    output = nmap.scan_top_ports(target)

    # Getting target IP, since the target is key is dynamic
    # We need to grab only target IP address to enumerate results object
    keys = []
    for key in output.keys():
        keys.append(key)
    
    results = output[keys[0]]['ports']
    return results