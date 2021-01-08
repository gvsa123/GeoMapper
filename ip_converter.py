from ip2geotools.databases.noncommercial import DbIpCity
from ip2geotools.errors import ServiceError
from ip2geotools.errors import InvalidRequestError

import pickle
import requests

URL = 'http://api.db-ip.com/v2/free'

# Check daily quota limit
def remaining_queries(URL):
    """Check daily quota limit before converting ip addresses"""

    with requests.get(URL) as r:
        json_data = r.json()
        limit = json_data['queriesLeft']
    
    # print("Daily quota: {}".format(limit))
    return limit

limit = remaining_queries(URL=URL)

def batch_query(IP_LIST, URL, LIMIT=limit):
    """Batch query ip database via http"""

    if len(IP_LIST) < LIMIT:
        print("Constructing query:")
        query = URL + '/' + ','.join(IP_LIST)
        print("QUERY : {}\n".format(query))

        # http batch request
        with requests.get(query) as r:
            json_data = r.json()
    
    elif len(IP_LIST) >= query:
        print("Query will exceed daily quota. Be nice.")
    
    return json_data

def json_parser(DATA):
    
    """Parse named locations from json_data
    
    Parameters
    ----------
    DATA : Dictionary with ip_addresses as keys and location
    data as values    
    Example
    -------
    {'107.189.10.246': {'continentCode': 'EU', 'continentName': 'Europe',
     'countryCode': 'LU', 'countryName': 'Luxembourg', 'stateProv':
     'Mersch', 'city': 'Bissen'}
     
     Output
     ------
    """
    for ip in DATA.keys():
        try:
            print(DATA[ip]['countryName'])
        except KeyError as ke:
            print(ke)
            pass
    

def ip_to_coord(IP_LIST, LIMIT=limit):
    """Convert IP_LIST to COORDINATES - the long and slow way
    TODO:
    - deprecate with batch_query
    """

    if len(IP_LIST) < LIMIT:
        COORDINATES = set() # no duplicate coordinate.
        error_counter = 0
        print(f"Converting {len(IP_LIST)}:")
        for ip in IP_LIST:
            try:
                response = DbIpCity.get(ip, api_key='free') # DbIpCity ServiceError?
                c = (response.latitude, response.longitude)
                COORDINATES.add(c)
                print(f"{ip} ---> ({response.latitude},{response.longitude})")
            except KeyError as err:
                print(f"KeyError: {err} {ip}")
                error_counter += 1
                pass
            except ServiceError as err:
                print(f"ServiceError: {err}")
                error_counter += 1
                break
            except InvalidRequestError as err:
                print(f"InvalidRequestError: {err}")
                error_counter += 1
                pass
        print(f"Processed {len(COORDINATES)}.")
        print(f"{error_counter} errors.")

    else:
        raise Exception("Daily quota not enough.")
    
    with open('./Data/COORDINATES.p', 'wb') as f:
        pickle.dump(COORDINATES, f)
        print(f)
    
    return COORDINATES

def main():
    """Convert IP_LIST to COORDINATESformat"""

    if limit > 32: # Check limit before doing anything!
        from query_database import failed_logins
        from import_coordinates import ip_from_query, df_to_list
        from ip_converter import json_parser
    
        QUERY_RESULT = failed_logins()
        ip_dataframe = ip_from_query(QUERY_RESULT)
        IP_LIST = df_to_list(ip_dataframe)
        json_data = batch_query(IP_LIST=IP_LIST[:31], URL=URL)

        json_parser(json_data)

        # COORDINATES = ip_to_coord(IP_LIST, query)

        # return COORDINATES

if __name__ == "__main__":
    main()