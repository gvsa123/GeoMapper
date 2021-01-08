from ip2geotools.databases.noncommercial import DbIpCity
import pickle
IP = pickle.load(open('./Data/short_list.p', 'rb'))
print(IP, len(IP))
response = DbIpCity.get(IP, api_key='free') # DbIpCity ServiceError?
print(response, len(response))
