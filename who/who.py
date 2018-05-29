#!/bin/python3
import whois
import sys
import socket
import dns.resolver
from termcolor import colored

domain = whois.whois('lyuboslavzahariev.com')



def prn(*args):
    
    for x in args:
        print()
        print('========================================================================')
        print()
        print(x)
    print()
    print('========================================================================')
    print('========================================================================')
    print('========================================================================')
    print('========================================================================')
    print()



def who(dn):
    w = whois.whois(dn)
    print()
    print(colored('========================================================================','green'))
    print()
    print(w.domain_name)
    print()
    print('========================================================================')
    print()
    
    try:
        print(w.expiration_date[0])
    except:
        print(w.expiration_date)
    print(w.registrar)
    print()
    print('========================================================================')
    print()
    for x in w.status:
        print(x)

    print()
    print('========================================================================')
    print('========================================================================')
    print('========================================================================')
    print('========================================================================')
    print()

    for x in w.name_servers:
        print(x)
    print()
    print('========================================================================')
    print('========================================================================')
    print('========================================================================')
    print('========================================================================')
    print()

def dig(dn):
    for x in dns.resolver.query(dn):
        print(x)
    print('========================================================================')
    for x in dns.resolver.query(dn, "MX"):
        print(x)
        for y in dns.resolver.query(str(x.exchange)):
            print(y)
    print('========================================================================')
    print('========================================================================')
    print('========================================================================')
    print(colored('========================================================================','red'))
    print()


for x in sys.argv:
    if x!=sys.argv[0]:
        who(x)
        dig(x)
