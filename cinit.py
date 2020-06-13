#!/usr/bin/python3

# Standard Libs
from netmiko import ConnectHandler
from sys     import exit
from getpass import getpass
import logging

# Own lib
import lib_config as libco
import args       as args 

logging.basicConfig(filename='debug.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

passwd  = getpass()


def main():

    args = libco.parser.parse_args()

    for indx, port in enumerate(args.ports):

        output = ''

        #dev = ConnectHandler(device_type         = 'cisco_ios_telnet',
        #                     host                =  args.host,
        #                     port                =  port,
        #                     username            = 'thalo',
        #                     password            =  passwd,
        #                     global_delay_factor =  4,
        #                     secret              =  passwd,
        #                     session_log         = "output.txt",
        #                     verbose             =  True)

        CMD = libco.init_config(args.device, (indx + 1), passwd)

        print("[!!] - Configure Device nr. {} - {}".format((indx + 1), CMD[0]))

        #output += dev.enable()
        #output += dev.send_config_set(CMD)
        #output += dev.save_config(libco.SAVE)

        print("{}".format(output))
        print("----------- END -----------")
        #dev.disconnect()

if __name__ == '__main__':
    main()
