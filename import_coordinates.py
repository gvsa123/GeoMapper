import mapper
import pandas as pd
import time

from ip2geotools.databases.noncommercial import DbIpCity
from ip2geotools.errors import ServiceError
from ip2geotools.errors import InvalidRequestError

CSV_FILE = './Data/failed_logins.csv'

def ip_from_csv(CSV_FILE):
    """Import COORDINATES from csvfile. Removes duplicates.
    TODO:
    - can be depricated when database pipe functional
    """

    ip_dataframe = pd.read_csv(
        CSV_FILE,
        delimiter='\t',
        names=['id', 'user_id', 'user_login', 'failed_login_date', 'login_attempt_ip'],
        usecols=['login_date', 'ip_address']
    ).drop_duplicates(subset='ip_address')
    
    return ip_dataframe

def ip_from_query(QUERY_RESULT):
    """Takes the result of query_database and converts into df of ip_address
    """
    ip_dataframe = pd.DataFrame(
        QUERY_RESULT,
        columns=['id', 'user_id', 'user_login', 'failed_login_date', 'login_attempt_ip'],    
    )

    ip_dataframe.drop_duplicates(subset='login_attempt_ip', inplace=True)
    print("duplicates removed {}".format(ip_dataframe.shape))

    return ip_dataframe['login_attempt_ip']

def df_to_list(ip_dataframe):
    """Convert ip_dataframe to list of ip addresses
    Parameters
    ----------
    ip_dataframe : pandas dataframe
    """
    IP_LIST = ip_dataframe.values.tolist()
    print(f"Converted {len(IP_LIST)} ip_addresses to list")

    return IP_LIST

def ip_to_coord(IP_LIST):
    """Convert IP_LIST to COORDINATES
    TODO:
    - create KeyError counter? Or limit accuracy of COORDINATES?
    """
    COORDINATES = set()
    print(f"Converting {len(IP_LIST)} to COORDINATES")
    for ip in IP_LIST:
        try:
            response = DbIpCity.get(ip, api_key='free') # DbIpCity ServiceError?
            c = (response.latitude, response.longitude)
            COORDINATES.add(c)
            print(f"{ip} ---> ({response.latitude},{response.longitude})")
            time.sleep(1)
        except KeyError as e:
            print(f"Error: {e}")
            pass
        except ServiceError as e:
            print(f"Error: {e}")
            pass
        except InvalidRequestError as e:
            print(f"Error: {e}")
            pass
    print(f"Processing {len(COORDINATES)} COORDINATES.")
    return COORDINATES

def main():
    from locator import point_extractor
    from mapper import geo_mapping
    from reverse_lookup import coordinate_locator
    from query_database import failed_logins
    
    QUERY_RESULT = failed_logins()
    ip_dataframe = ip_from_query(QUERY_RESULT)
    IP_LIST = df_to_list(ip_dataframe)
    raw_coordinates = ip_to_coord(IP_LIST)
    LOCATIONS = [coordinate_locator(c) for c in raw_coordinates]
    COORDINATES = point_extractor(LOCATIONS)
    geo_mapping(COORDINATES)

if __name__ == "__main__":
    main()
