import jsonrpclib
from pprint import pprint

import pyeapi

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# This will trust the self-signed Arista SSL certificate.

username  = 'pyclass'
password =  '88newclass'
ip = '184.105.247.72' 
port = '443'


pynet_sw3 = pyeapi.connect_to("pynet-sw3")

show_interfaces = pynet_sw3.enable("show interfaces")

show_interfaces = show_interfaces[0]



result = show_interfaces["result"]

interfaces = result["interfaces"]

for key in interfaces:
    if key != 'Vlan1':
        print(key)
        print("     In Octets: ", interfaces[key]["interfaceCounters"]["inOctets"])
        print("     Out Octets: ", interfaces[key]["interfaceCounters"]["outOctets"])


