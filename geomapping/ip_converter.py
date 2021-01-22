from ip2geotools.databases.noncommercial import DbIpCity
from ip2geotools.errors import ServiceError
from ip2geotools.errors import InvalidRequestError

import pickle
import requests

# Check daily quota limit
def remaining_queries(URL):

    """Check daily quota limit before converting ip addresses"""

    with requests.get(URL) as r:
        json_data = r.json()
        limit = json_data['queriesLeft']
    
    # print("Daily quota: {}".format(limit))
    return limit

def split_query(IP_LIST):
    """Limit batch_query length
    Returns
    -------
    temp_ip, over_ip placeholders

    TODO:
    - add functionality to return multiple batch queries of len=32 each
    """
    
    if len(IP_LIST) > 32:
        temp_ip = IP_LIST[:32]
        over_ip = IP_LIST[32:]
    
    return temp_ip, over_ip

def construct_query(IP_LIST, URL):
    """Create query string"""

    print("Constructing query:")
    try:
        if len(IP_LIST) == 0:
            print(IP_LIST)
        elif len(IP_LIST) == 1:
            query = URL + '/' + IP_LIST[0]
        elif len(IP_LIST) > 2:
            query = URL + '/' + ','.join(IP_LIST)
    finally:
        print(query)
        
        return query

def batch_request(QUERY):
    """Batch request"""
    # http batch request
    with requests.get(QUERY) as r:
        json_data = r.json()
    
    return json_data

def batch_query(IP_LIST, URL, LIMIT=32):
    """Batch query ip database via http"""
    
    print(f"{len(IP_LIST)} in IP_LIST\n")
    
    query = construct_query(IP_LIST, URL)            
    json_data = batch_request(query)

    return json_data
    
    # try:
    #     if len(IP_LIST) <= LIMIT:
    #         query = construct_query(IP_LIST, URL)
            
    #         json_data = batch_request(query)
        
    #     elif len(IP_LIST) > LIMIT and len(IP_LIST) < 64:
    #         """How to handle 3+ list divisions?"""
            
    #         json_data = batch_request(query)

    #         # USE DATA = [] AS PLACEHOLDER
            
    #         temp_ip, over_ip = split_query(IP_LIST)
    #         MASTER_IP_LIST = [temp_ip, over_ip]

    #         for IPL in MASTER_IP_LIST:
    #             query = construct_query(IPL, URL)

    #         json_data = batch_request(query)


    #         # http batch request
    #         with requests.get(query) as r:
    #             json_data = r.json()
    #     else:
    #         json_data = batch_request(query)
    #         print("Query will exceed daily quota. Be nice.")

    
    # finally:
        
    #     return json_data

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
    ADDR = set()

    try:
        for ip in DATA.keys():
            try:
                address = "{}, {}, {}".format(DATA[ip]['city'], DATA[ip]['stateProv'], DATA[ip]['countryName'])
                ADDR.add(address)
            except KeyError as ke:
                print("Missing: {}".format(ke))
                pass
    except TypeError as te:
        assert len(ADDR) == 0, 'ADDR not empty'
        address = "{}, {}, {}".format(DATA['city'], DATA['stateProv'], DATA['countryName'])
        ADDR.add(address)

    return ADDR
    
def ip_to_coord(IP_LIST, LIMIT=32):
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
    
    with open('./data/COORDINATES.p', 'wb') as f:
        pickle.dump(COORDINATES, f)
        print(f)
    
    return COORDINATES
