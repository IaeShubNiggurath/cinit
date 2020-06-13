import argparse

# VARS
DOT1Q          = 'switchport trunk encapsulation dot1q'
INTERFACE      = 'interface gig'
SAVE           = "write mem"

# LISTS
INT_LIST_TRUNK = []
CHANNEL_GROUP  = []

hostnames = {
    'dist'  :  'DIST',
    'core'  :  'CORE',
    'router':  'R',
}


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--ports", help='the list of porst (telnet/gns3 working)', nargs='+')

parser.add_argument("-v", "--VLID", help='vlan id e.c. vlan 10',  action="store", required=False)

parser.add_argument("-t", "--trunks", help='trunk iface list',  action="append", required=False)

parser.add_argument("-e", "--etherchannel", help='etherchannel',  action="store", required=False)

parser.add_argument("-d", "--device", help='what kind of netword device', action="store", required=False)

parser.add_argument("-H", "--host", help='IP or FQDN', action="store", default="127.0.0.1", required=False)


parser.add_argument("-i", "--init", help='init device type',
                                    default=False,
                                    required=False,
                                    action='store_true')

def init_config(device, counter, passwd):

    ADDUSER = 'username thalo privilege 15 secret {}'.format(passwd)
    SECRET  = 'enable secret {}'.format(passwd)
    DOMAIN  = 'ip domain-name getent.lab'
    SSH     = 'crypto key generate rsa modulus 4096'

    if device in hostnames:
        filename = "{}-{}-init.txt".format(device, counter)
        hostname = "hostname {}{}".format(hostnames[device], counter)

    with open(filename, 'w') as cfg:
        cfg.write('!\n!\n!\n' + hostname + '\n')
        cfg.write('!\n!\n!\n' + ADDUSER + '\n')
        cfg.write('!\n!\n!\n' + SECRET + '\n')
        cfg.write('!\n!\n!\n' + DOMAIN + '\n')
        cfg.write('!\n!\n!\n' + SSH + '\n')
        cfg.write('!\n!\n!\nline console 0\n login local\n logging synchronous\n')
        cfg.write('!\n!\n!\nline vty 0 10\n transport input ssh telnet\n login local!\n!\n!\n')

    return filename
