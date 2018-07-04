#!/uar/bin/env python

import getpass
import sys
import telnetlib
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def send_command(remote_conn, cmd):
   cmd = cmd.rstrip()
   remote_conn.write(cmd + '\n')
   time.sleep(1)
   output = remote_conn.read_very_eager()
   print output

def login(remote_conn, username, password):
   #remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
   output = remote_conn.read_until("Username:", TELNET_TIMEOUT)
   remote_conn.write(username + '\n')
   output += remote_conn.read_until("Password:", TELNET_TIMEOUT)
   remote_conn.write(password + '\n')
   return output

def main():
   ip_addr = '184.105.247.70'
   username = 'pyclass'
   password = '88newclass'

   remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
   output = login(remote_conn,username, password)   
   print output

   #time.sleep(1)
   #output = remote_conn.read_very_eager()

   output = send_command(remote_conn, 'terminal length 0')
  
   output = send_command(remote_conn, 'show ip interface brief')
   
   output = send_command(remote_conn, 'show version')

   list_intf = ["loop1999", "loop2999", "loop3999", "loop4999", "loop5999", "loop6999", "loop7999", "loop8999", "loop9999"]
   output = send_command(remote_conn, 'configure terminal')
   for intf in range(0, len(list_intf)):
      cmd = "interface " + list_intf[intf]
      output = send_command(remote_conn, cmd)
      cmd = "description " + list_intf[intf]
      output = send_command(remote_conn, cmd)
      intf += 1
   output = send_command(remote_conn, 'end')
   output = send_command(remote_conn, 'show ip interface brief')
   



   remote_conn.close()
 
if __name__ == "__main__":
    main()    
