# from ip2geotools.databases.noncommercial import DbIpCity
import pickle
import requests
import os

with open('./geomapping/data/short_list.p', 'rb') as file:
    IP_LIST = pickle.load(file)

def split_query(IP_LIST):
    """Limit batch_query length"""

    print(len(IP_LIST))
    if len(IP_LIST) > 32:
        temp_ip = IP_LIST[:32]
        over_ip = IP_LIST[32:]
    
    return temp_ip, over_ip

temp_ip, over_ip = split_query(IP_LIST)
print(len(temp_ip), len(over_ip))




# response = DbIpCity.get(IP, api_key='free') # DbIpCity ServiceError?
# print(response, len(response))
