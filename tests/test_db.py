import paramiko
from sshtunnel import SSHTunnelForwarder

tunnel = SSHTunnelForwarder(
    ('192.168.1.103', 2222),
    ssh_username='pi',
    ssh_password='B0c30131b6^',
    remote_bind_address=('localhost', 3306),
    local_bind_address=('127.0.0.1', 3306),
)

print(tunnel.is_active)
print(tunnel.is_alive)
