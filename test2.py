
#!/import/satools/bin/python3.5

# https://www.python-ldap.org/en/python-ldap-3.2.0/reference/ldap.html
# Check if there is Aria account, is user is still with Oracle
import sys
import ldap
import argparse

parser = argparse.ArgumentParser(
         formatter_class=argparse.RawTextHelpFormatter,
         description="Show Aria user")
account = parser.add_mutually_exclusive_group(required=True)
account.add_argument("-l", "--login", help="Login name")
account.add_argument("-e", "--email", help="email address")
args = parser.parse_args()
login=args.login
email=args.email

ARIA_SRV="aria-server.comp.com"
baseDN = "dc=comp,dc=com"
searchScope = ldap.SCOPE_SUBTREE # subtree search
retrieveAttributes = None

def main():
    """
    Check input and use as filter for search
    """
    if login:
        searchFilter = "uid=" + login
    elif email:
        searchFilter = "mail=" + email

    try:
        ldapobject = ldap.initialize('ldap://' + ARIA_SRV)
        ldapobject.protocol_version = ldap.VERSION3
        l_search = ldapobject.search(baseDN, searchScope, searchFilter, retrieveAttributes)
        result_status, result_data = ldapobject.result(l_search, 0)
        #print(type(result_data)) #list
        #print(result_data)
        try:
            #print(type(result_data[0][1]))  # dict
            #print((result_data[0][1]))
            if "employeetype"  in result_data[0][1]:
                print("Employee type: " + (result_data[0][1])["employeetype"][0].decode())
            else:
                print("Employee type: none")
            if "uid" in result_data[0][1]:
                print("Aria login: " + (result_data[0][1])["uid"][0].decode())
            else:
                print("Ari alogin: none")
            if "mail" in result_data[0][1]:
                print("Aria email: " + (result_data[0][1])["mail"][0].decode())
            else:
                print("Ari email: none")
            if "displayname" in result_data[0][1]:
                print("Display name: " + (result_data[0][1])["displayname"][0].decode())
            else:
                print("Display name: none")
            if "title" in result_data[0][1]:
                print("Title: " + (result_data[0][1])["title"][0].decode())
            else:
                print("Title: none")
            if "telephonenumber" in result_data[0][1]:
                print("Phone: " + (result_data[0][1])["telephonenumber"][0].decode())
            else:
                print("Phone: none")
            if "city" in result_data[0][1]:
                print("City: " + (result_data[0][1])["city"][0].decode())
            else:
                print("City: none")
            if "manager" in result_data[0][1]:
                print("User's manager: " + (result_data[0][1])["manager"][0].decode())
            else:
                print("User's manager: none")
            if "o" in result_data[0][1]:
                print("Organization: " + (result_data[0][1])["o"][0].decode())
            else:
                print("Organization: none")
        except:
            sys.exit("A user is not with Oracle.")
    except ldap.LDAPError as err:
        print("ldap.LDAPError: {0}".format(err))

if __name__ == '__main__':
    main()

sys.exit(0)