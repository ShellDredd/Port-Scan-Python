#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Author: || ShellDredd ||
#Twitter: @ShellDredd
#Web site: hhttps://shelldredd.github.io/

import nmap, os, sys

#Colors:
clear='\033[0;m'
purple='\x1b[1;35m'
def purple2(skk): print("\x1b[1;35m {}\033[01m" .format(skk) + clear)

#Banner:
print("\n")
banner = os.system('toilet -f pagga --metal "ShellDredd"')

#Header:
print("")
purple2(' PURPLE PAPERS     ---     @SHELLDREDD')
purple2('         # Nmap Script module')
purple2('✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪')


try:
    sexy = nmap.PortScanner()         
except nmap.PortScannerError:
    print('Nmap not found Baby - Install package.', sys.exc_info()[0])
    sys.exit(0)
except:
    print("Error Baby : ", sys.exc_info()[0])
    sys.exit(0)


ip = input(purple + '\nˁ˚ᴥ˚ˀ I need a IP -_-_->\t' + clear)
purple2("\n[*] Scanning ports and services for IP:\t" + clear + ip + purple + "\n\n[#] Wait a moment please.\n")

sexy = nmap.PortScanner()
sexy.scan(hosts=ip, arguments='-sCV -O -p- ')
os.system('clear')

#Extract - Scanning funtion:
for host in sexy.all_hosts():    

    print(purple + '\nˁ˚ᴥ˚ˀ Host : %s (%s)\n' % (host, sexy[host].state()) + clear)
    
    for proto in sexy[host].all_protocols():
        print('Protocolo : %s' % proto)

        lport = list(sexy[host][proto].keys())
        lport.sort()
        for port in lport:
            print('Port : %s\tInfo : %s\t%s\t%s\t%s\t%s\t%s' % (port, sexy[host][proto][port]['state'], sexy[host][proto][port]['name'],
                  sexy[host][proto][port]['reason'], sexy[host][proto][port]['version'], sexy[host][proto][port]['product'], 
                  sexy[host][proto][port]['extrainfo']))

#Output result:
print(purple + "\nˁ˚ᴥ˚ˀ Port Information:\n" + clear)
print('PORT TCP : %s' % (sexy[host].all_tcp()) + '\tPORT UDP : %s' % (sexy[host].all_udp()))
print('PORT SCTP : %s' % (sexy[host].all_sctp()) + '\tIPs : %s' % (sexy[host].all_ip()))


#CSV format for report:
print(purple + '\nˁ˚ᴥ˚ˀ Report in csv format stored in the file ' + clear + '-nmap_report_csv-\n')
csv=sexy.csv()
print(csv, file=open('nmap_report_csv','w'))


# Maritrini12345 sponsors this script (✿ ♥‿♥) 
