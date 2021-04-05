# geomapper

The project is an exercise in creating a data pipeline, basic web development and data processing using python. It queries a MariaDB server for failed wordpress login attempts, converts the logged ip addresses into geolocations, and outputs an html map using a flask and jinja2 framework.

You need to supply it with a proper config.ini to be able to connect to your database:

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
![sample out](/app/static/sample_output.png)
