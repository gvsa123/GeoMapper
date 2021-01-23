import configparser
import logging
import os
import paramiko
import pymysql.cursors
import time

from sshtunnel import SSHTunnelForwarder

"""CONFIGURATION"""
# move to file
path = os.getcwd() + '/geomapping/config.ini'
config = configparser.ConfigParser()
config.read(path)
SSH_USERNAME = config['SSHTUNNEL']['ssh_username']
SSH_PASSWORD = config['SSHTUNNEL']['ssh_password']
SSH_PRIVATE_KEY_PASSWORD = config['SSHTUNNEL']['ssh_private_key_password']
SQL_USERNAME = config['MYSQL']['sql_username']
SQL_PASSWORD = config['MYSQL']['sql_password']
DB = config['MYSQL']['db']

"""Password required error ---> save your sanity; generate new key?"""
PKEY_PATH = os.environ['HOME'] + '/.ssh/id_rsa'
PKEY = paramiko.RSAKey.from_private_key_file(PKEY_PATH, password=SSH_PRIVATE_KEY_PASSWORD)

def failed_logins():
    """Query wordpress database for failed login attempts

    Returns
    -------
    sql : tuple; raw sql output
    """
    try:
        # Create sshtunnel
        print("initiate query_database")
        with SSHTunnelForwarder(
                ('192.168.1.103', 2222),
                ssh_username=SSH_USERNAME,
                ssh_pkey=PKEY,
                remote_bind_address=('localhost', 3306),
                local_bind_address=('127.0.0.1', 3306),
            ) as tunnel:

            if tunnel.is_alive == True:
                print("connecting to database")
                time.sleep(1)

                # Connect to the database
                connection = pymysql.connect(
                    user= SQL_USERNAME,
                    password= SQL_PASSWORD,
                    db= DB,
                )
                
                print("sql connection established")

            with connection.cursor() as cursor:
                sql_query = ('SELECT * FROM gvsa123aiowps_failed_logins WHERE failed_login_date BETWEEN DATE_SUB(NOW(), INTERVAL 1 DAY) AND NOW()')
                cursor.execute(sql_query)
                result = cursor.fetchall()
                assert len(result) > 0, "result empty"
                print("database query success")

        if connection: # catch UnboundLocalError
            connection.close()
            print("connection closed")

        if tunnel:
            tunnel.stop(force=True)
            print("tunnel closed")

    except paramiko.PasswordRequiredException:
        print('arg!')
            
    finally:
        
        return result

def main():
    print("Running failed_logins...")
    failed_logins()
    
if __name__ == "__main__":
    path = './config.ini'
    main()