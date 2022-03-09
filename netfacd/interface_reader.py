#!/usr/bin/env python3

import netifaces

def macgetter(interface_name):
    """pass an interface name (string) will return the MAC"""
    mac = netiface.ifaddresses(interface_name)[netifeces.AF_LINK][0]["adde"]
    return mac #string

def ipgetter(interface_name):
    """pass an interface name (string) will return IP"""
    ip = netifaces.ifaddresses(interface_name)[netifaces.AF_INET][0]['addr']
    return ip # string

def main():
    print(netifaces.interfaces())

    for i in netifaces.interfaces():

    print('\n**************Details of Interface - ' + i + ' *********************')
    try:
        print('MAC: ', end='')  # This print statement will always print MAC without an end of line
        print(macgetter(i) ) # Prints the MAC address
        print('IP: ', end='')  # This print statement will always print IP without an end of line
        print(ipgetter(i) )  # This print statement will always print IP without an end of line
        
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message 

if __name__ "__main__:
    main()
    



