import configparser
import os
import paramiko
import pymysql.cursors
from sshtunnel import SSHTunnelForwarder
import time

"""CONFIGURATION"""
# Convert to paramiko key
pkey = os.environ.get('HOME') + '/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(filename=pkey, password='B0c30131b6^')

# ConfigParser
config = configparser.ConfigParser()
config.read('config.ini')
ssh_username = config['SSHTUNNEL']['ssh_username']
sql_username = config['MYSQL']['sql_username']
sql_password = config['MYSQL']['sql_password']
db = config['MYSQL']['db']

def failed_logins():
    """Query wordpress db for failed_logins
    Returns
    -------
    sql : tuple; raw sql output
    """
    try:
        # Create sshtunnel with bound port
        print("\nInitiate query_database...")

        with SSHTunnelForwarder(
                ('192.168.1.103', 2222),
                ssh_username=ssh_username,
                ssh_pkey=key,
                remote_bind_address=('localhost', 3306),
                local_bind_address=('127.0.0.1', 3306),
            ) as tunnel:
            
            # Connect to the database
            connection = pymysql.connect(
                user= sql_username,
                password= sql_password,
                db= db,
                # cursorclass=pymysql.cursors.DictCursor
            )

            time.sleep(.5)

            with connection.cursor() as cursor:
                # SHOW DATABASES
                sql = ("SELECT * FROM gvsa123aiowps_failed_logins WHERE failed_login_date BETWEEN DATE_SUB(NOW(), INTERVAL 1 MONTH) AND NOW()")
                # sql = ("SELECT * FROM gvsa123aiowps_failed_logins")
                cursor.execute(sql)
                result = cursor.fetchall()
            
            time.sleep(.5)
    finally:
        if connection:
            connection.close()
            print("Connection closed.")
            time.sleep(.5)
        if tunnel:
            tunnel.stop(force=True)
            print("Tunnel closed.")
            time.sleep(.5)
        print("Database query success.\n")
        time.sleep(.5)

        return result

def main():
    print("Running failed_logins...")
    print(failed_logins())
    
    
if __name__ == "__main__":
    main()