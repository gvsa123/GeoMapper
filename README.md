# geomapper

The project is an exercise in locating and mapping failed login attempts on servers using a flask framework. It takes in ip addresses and converts them into location addresses that can be mapped and rendered in html.

You need to supply it with a config.ini with the following:

## query_database config.ini

[SSHTUNNEL]  
ssh_username="SSH_USERNAME"  
ssh_password="SSH_PASSWORD"  
ssh_private_key_password="SSH_PRIVATE_KEY_PASSWORD"  
  
[MYSQL]  
sql_username="SQL_USERNAME"  
sql_password="SQL_PASSWORD"  
db="DB"

## sample output
![sample out]
(/app/static/sample_output.png)
