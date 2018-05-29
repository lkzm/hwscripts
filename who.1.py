#!/bin/python3
import whois
import sys
import socket
import dns.resolver
from termcolor import colored
import requests



   


def who(dn):
    w = whois.whois(dn)
    temp = '''=============================================================================
    =============================================================================
    =============================================================================
    =============================================================================
    ============================================================================='''
    temp += '''
    %s''' % (str(w.registrar))
    temp += '''
    %s''' %(str(w.domain_name))
    temp +=('''
    %s''') % (str(w.expiration_date))
    temp += ('''
    %s''') % (str(w.status))
    temp +=('''
    %s''') % (str(w.name_servers))
    return temp

def dig(dn):
    temp = '''=============================================================================
    =============================================================================
    =============================================================================
    =============================================================================
    ============================================================================='''


    temp += '''
    %s''' % (str(dns.resolver.query(dn)))
    temp += '''
    %s''' % (str(dns.resolver.query(dn, "MX")))

    return temp

for x in sys.argv:
    if x!=sys.argv[0]:
        temp=who(x)
        temp += dig(x)
        payload = {'domainName': x, 'whois': temp, 'ticket': 'it works fag'}
        r = requests.post('https://prod-45.westus.logic.azure.com:443/workflows/e760c74c3c8644d089fa215dd53eb606/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=SfH9jkErvjzVwp3UoXklfjLwldtCsHGRN2v9eI-eIjg', params=payload)
        print(r.status_code, r.reason)       
        print(r.text)
