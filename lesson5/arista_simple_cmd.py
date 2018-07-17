import jsonrpclib
from pprint import pprint

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# This will trust the self-signed Arista SSL certificate.

username  = 'pyclass'
password =  '88newclass'
ip = '184.105.247.72' 
port = '443'

switch_url = "https://{}:{}@{}:{}".format(username, password, ip, port)
#then switch_url = 'https://pyclass:88newclass@184.105.247.72:443'
switch_url = switch_url + '/command-api'

remote_connect = jsonrpclib.Server(switch_url)
response = remote_connect.runCmds(1, ['show version', 'show arp', 'show hostname'])

pprint(response)

