
from ldap3 import ALL, Connection, Server
from ldap3.core.exceptions import LDAPException

username = "mohanned"
password = "MO-che<123.@&."
ldap_base = "dc=ssir,dc=local"

server = Server(
    host="ldaps://192.168.56.105",
    port=50000,
    use_ssl=True,
    get_info=ALL,
)

try:
    with Connection(
        server=server,
        authentication="SIMPLE",
        user=f"uid={username},{ldap_base}",
        password=password,
        read_only=True,
        ) as connection:
            print(connection.result)  # "success" if bind is ok

except LDAPException as e:
    print(server.info)