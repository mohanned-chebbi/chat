from ldap3 import Server, Connection, ALL, NTLM

# Define the server and the connection
server = Server('WIN-7AVUSDN4KIH.ssir.local', port=50000, get_info=ALL)
conn = Connection(server, user='<ssir\Administrator>', password='<LAbib<3.>', authentication=NTLM)

# Start the connection
conn.bind()

# Check if the connection was successful
if conn.result["description"] == "success":
    print("Connected to the AD LDS instance successfully")
else:
    print("Error connecting to the AD LDS instance: ", conn.result)