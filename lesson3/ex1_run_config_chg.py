

import os.path
from datetime import datetime
from getpass import getpass
from collections import namedtuple

from snmp_helper import snmp_get_oid_v3, snmp_extract
from email_helper import send_mail

import smtplib
import email_helper


NetworkDevice = namedtuple("NetworkDevice", "uptime last_changed run_config_changed")
pynet_rtr1 = ("184.105.247.70", 161)
a_device = pynet_rtr1
snmp_user = ('pysnmp', 'galileo1', 'galileo1')

def send_mail(recipient, subject, message, sender):
    '''
    Simple function to help simplify sending SMTP email

    Assumes a mailserver is available on localhost
    '''
    
    from email.mime.text import MIMEText
    message = MIMEText(message)
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = recipient

    # Create SMTP connection object to localhost
    smtp_conn = smtplib.SMTP('localhost')

    # Send the email
    smtp_conn.sendmail(sender, recipient, message.as_string())

    # Close SMTP connection
    smtp_conn.quit()
    return True



def get_snmp_system_name(a_device, snmp_user):
    """Use SNMP to obtain the system name."""
    sys_name_oid = '1.3.6.1.2.1.1.5.0'
    return snmp_extract(snmp_get_oid_v3(a_device, snmp_user, oid=sys_name_oid))


def get_snmp_uptime(a_device, snmp_user):
    """Use SNMP to obtain the system uptime."""
    sys_uptime_oid = '1.3.6.1.2.1.1.3.0'
    return int(snmp_extract(snmp_get_oid_v3(a_device, snmp_user, oid=sys_uptime_oid)))


def create_new_device(device_name, uptime, last_changed):
    """Create new Network Device."""
    dots_to_print = (35 - len(device_name)) * '.'
    print("{} {}".format(device_name, dots_to_print))
    print("saving new device")
    return NetworkDevice(uptime, last_changed, False)

def main():
    run_last_changed = '1.3.6.1.4.1.9.9.43.1.1.1.0'
    uptime = get_snmp_uptime(a_device, snmp_user)
    device_name = get_snmp_system_name(a_device, snmp_user)
    last_changed = int(snmp_extract(snmp_get_oid_v3(a_device, snmp_user, oid=run_last_changed)))
    get_snmp_system_name(a_device, snmp_user)
    get_snmp_uptime(a_device, snmp_user)
    create_new_device(device_name, uptime, last_changed)

    current_time = datetime.now()
    recipient = 'mammouhb@gmail.com'
    subject = 'Device {} was modified'.format(device_name)
    message = '''
    
    The running configuration of {} was modified.
    This change was detected at: {}
    
    
    Regards,
    
    Bouchaib
    
    '''.format(device_name, current_time)
    
    sender = 'mammouhb@gmail.com'
    email_helper.send_mail(recipient, subject, message, sender) 

if __name__ == '__main__':
    main()

