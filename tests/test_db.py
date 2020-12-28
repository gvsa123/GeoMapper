import mysql.connector
from sshtunnel import SSHTunnelForwarder

"""
does not work for mysql.connector:
- localhost
- 127.0.0.1
- 192.168.1.102
"""
server = SSHTunnelForwarder(
    ('192.168.1.103', 2222),
    ssh_username='pi',
    ssh_password='B0c30131b6^',
    remote_bind_address=('localhost', 8080), 
)

server.start()

PORT = server.local_bind_port

print("server.local_bind_port {}".format(server.local_bind_port))