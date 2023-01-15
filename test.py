import ldap
from flask import Flask, render_template , request, redirect, session, url_for
import mysql.connector
import hashlib
import sys
# Connect to the LDAP server
ldap_conn = ldap.initialize("ldap://192.168.56.105:50000")

try:
    ldap_conn.simple_bind("mohanned@ssir.local", "MO-che<123.@&a")
except (ldap.INVALID_CREDENTIALS):
    print("This password is incorrect!")
    sys.exit(3)
print("Authentization successful")
results = ldap_conn.search("dc=ssir,dc=local", ldap.SCOPE_SUBTREE,'(objectClass=*)',['mail'])

# Print the search results
print(results)
'''
base="dc=ssir,dc=local"
attrs = "*"
# Bind to the server using a DN and password
ldap_conn.bind("mohanned@ssir.local", "MO-che<123.@&")
print(ldap_conn)
# Search the directory for a user
#result = ldap_conn.search("dc=ssir,dc=local", ldap.SCOPE_SUBTREE, "uid=1234")
results = ldap_conn.search_s("dc=ssir,dc=local", ldap.SCOPE_SUBTREE,'(objectClass=*)',['mail'])

# Print the search results
print(results)

# Unbind from the server
#ldap_conn.unbind_s()

'''