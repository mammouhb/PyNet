import jsonrpclib
from pprint import pprint

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# This will trust the self-signed Arista SSL certificate.

username  = 'pyclass'
password =  '88newclass'
ip = '184.105.247.72' 
port = '443'

#
#
#
#show commands
#
#
#

switch_url = "https://{}:{}@{}:{}".format(username, password, ip, port)
#then switch_url = 'https://pyclass:88newclass@184.105.247.72:443'
switch_url = switch_url + '/command-api'

remote_connect = jsonrpclib.Server(switch_url)
response = remote_connect.runCmds(1, ['show version', 'show arp', 'show hostname'])

pprint(response)

#
#
#
#Config change
#
#
#

commands = []

commands.append('vlan 225')
commands.insert(0,'configure terminal')
commands.insert(0, {'cmd' : 'enable', 'input': ''})
commands.append('name green')
remote_connect.runCmds(1, commands)

commands[2] = 'vlan 226'
commands[3] = 'name black'
remote_connect.runCmds(1, commands)

commands[2] = 'vlan 227'
commands[3] = 'name yellow'
remote_connect.runCmds(1, commands)

commands[2] = 'vrf definition test_api_bouch'
commands[3] = 'rd 321:123'
remote_connect.runCmds(1, commands)

commands[2] = 'interface loopback321'
commands[3] = 'vrf forwarding test_api_bouch'
remote_connect.runCmds(1, commands)


#
#
#
#Making configuration changes via eAPI
#
#
#
import pyeapi

pynet_sw3 = pyeapi.connect_to("pynet-sw3")

# dir(pynet_sw3)  !!!! available commands

pynet_sw3.get_config()

config = pynet_sw3.get_config()

pprint(config)

show_version = pynet_sw3.enable("show version")

show_version = show_version[0]

pprint(show_version)

show_version = show_version["result"]

pprint(show_version)

show_arp = pynet_sw3.enable("show arp")

show_arp = show_arp[0]

show_arp =  show_arp["result"]
pprint(show_arp)

show_arp = show_arp["ipV4Neighbors"]
pprint(show_arp)

show_vlan = pynet_sw3.enable("show vlan")
pprint(show_vlan)

cmds = ['vlan 225', 'name green', 'vlan 226', 'name black']
pynet_sw3.config(cmds)

pynet_sw3.enable("write memory")
output = pynet_sw3.enable("write memory")
pprint(output)


show_vlan = pynet_sw3.enable("show vlan")
pprint(show_vlan)

