import ldap

ldap_server="192.168.1.81"
username="hadir"
password="HS123@nabel<3."
	# the following is the user_dn format provided by the ldap server
user_dn = "uid="+username+",ou=Tekup,dc=MOHANNED,dc=local"
	# adjust this to your base dn for searching
base_dn = "dc=MOHANNED,dc=local"
connect = ldap.initialize(ldap_server)
search_filter = "uid="+username
try:
	#if authentication successful, get the full user data
	connect.bind_s(user_dn,password)
	result = connect.search_s(base_dn,ldap.SCOPE_SUBTREE,search_filter)
		# return all user data results
	connect.unbind_s()
	print (result)
except ldap.LDAPError:
	connect.unbind_s()
	print ("authentication error")