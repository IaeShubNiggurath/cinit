

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--ports", help='the list of porst (telnet/gns3 working)',
                                     nargs='+')

parser.add_argument("-v", "--VLID", help='vlan id e.c. vlan 10',
                                    action="store",
                                    required=False)

parser.add_argument("-t", "--trunks", help='trunk iface list',
                                      action="append",
                                      required=False)

parser.add_argument("-e", "--etherchannel", help='etherchannel',
                                            action="store",
                                            required=False)

parser.add_argument("-d", "--device", help='what kind of netword device',
                                      action="store",
                                      required=False)

parser.add_argument("-H", "--host", help='IP or FQDN',
                                    action="store",
                                    default="127.0.0.1",
                                    required=False)


parser.add_argument("-i", "--init", help='init device type',
                                    default=False,
                                    required=False,
                                    action='store_true')
