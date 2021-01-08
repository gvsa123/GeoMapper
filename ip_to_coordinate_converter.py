from ip2geotools.databases.noncommercial import DbIpCity
from ip2geotools.errors import ServiceError
from ip2geotools.errors import InvalidRequestError

import pickle
import requests

URL = 'http://api.db-ip.com/v2/free'

def remaining_queries(URL):
    """Check daily quota limit before converting ip addresses"""

    with requests.get(URL) as r:
        data = r.json()
        query = data['queriesLeft']

    print(query)
    return query

query = remaining_queries(URL=URL)

def batch_query(IP_LIST, URL):
    """Batch query ip database via http"""
    
    print("Constructing query.")
    query = URL + '/' + ','.join(IP_LIST)
    print(query)

    with requests.get(query) as r:
        data = r.json()
        
    print(data)


def ip_to_coord(IP_LIST, query=query):
    """Convert IP_LIST to COORDINATES - the long and slow way"""

    if len(IP_LIST) < query:
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
    """Convert IP_LIST to COORDINATESformat
    TODO:
    - extract ip_address column from IP_LIST before passing to batch_query()
    """
    
    from query_database import failed_logins
    from import_coordinates import ip_from_query
    from import_coordinates import df_to_list

    # query = remaining_queries()
    
    QUERY_RESULT = failed_logins()
    ip_dataframe = ip_from_query(QUERY_RESULT)
    IP_LIST = df_to_list(ip_dataframe)

    # COORDINATES = ip_to_coord(IP_LIST, query)
    
    URL = 'http://api.db-ip.com/v2/free'
    # batch_query(IP_LIST=['172.219.34.170'], URL=URL)
    batch_query(IP_LIST=IP_LIST[:31], URL=URL)

    # return COORDINATES

if __name__ == "__main__":
    main()