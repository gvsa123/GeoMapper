import mapper
import pandas as pd
import time

from reverse_lookup import reverse_lookup
from mapper import geo_mapping
from locator import raw_location
from ip2geotools.databases.noncommercial import DbIpCity
from ip2geotools.databases.noncommercial import HostIP

CSV_FILE = './Data/failed_logins.csv'

def ip_from_csv(CSV_FILE):
    """Import COORDINATES from csvfile"""

    ip_dataframe = pd.read_csv(
        CSV_FILE,
        delimiter='\t',
        names=['id', 'success', 'user', 'login_date', 'ip_address'],
        usecols=['login_date', 'ip_address']
    ).drop_duplicates(subset='ip_address')
    
    return ip_dataframe

def ip_df_to_list(ip_dataframe):
    """Convert ip_dataframe to list of ip addresses
    Parameters
    ----------
    ip_dataframe : pandas dataframe
    """
    IP_LIST = ip_dataframe['ip_address'].values.tolist()
    print("IP_LIST : {}".format(len(IP_LIST)))

    return IP_LIST

def ip_to_coord(IP_LIST):
    """Convert IP_LIST to COORDINATES
    TODO:
    - create KeyError counter? Or limit accuracy of COORDINATES?
    """
    COORDINATES = []
    for ip in IP_LIST[15:20]:
        try:
            response = DbIpCity.get(ip, api_key='free') # DbIpCity ServiceError?
            c = (response.latitude, response.longitude)
            COORDINATES.append(c)
            print(f"{ip} ---> ({response.latitude},{response.longitude})")
            time.sleep(1)
        except KeyError as ke:
            print(f"KeyError: {ke}")
            pass
        except ip2geotools.errors.ServiceError as se:
            print(f"ServiceError: {se}")
            pass

    return COORDINATES

def main():
    ip_dataframe = ip_from_csv(CSV_FILE)
    IP_LIST = ip_df_to_list(ip_dataframe)
    raw_coordinates = ip_to_coord(IP_LIST)
    LOCATIONS = [reverse_lookup(c) for c in raw_coordinates]
    COORDINATES = raw_location(LOCATIONS)
    geo_mapping(COORDINATES)

if __name__ == "__main__":
    main()
