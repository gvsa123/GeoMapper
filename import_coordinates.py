import pandas as pd
import time

def ip_from_csv(CSV_FILE='./Data/failed_logins.csv'):
    """Import COORDINATES from csvfile. Removes duplicates.
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
    print("duplicates removed. {} unique ip aaddresses.".format(ip_dataframe.shape[0]))

    return ip_dataframe['login_attempt_ip']

def df_to_list(ip_dataframe):
    """Convert ip_dataframe to list of ip addresses
    Parameters
    ----------
    ip_dataframe : pandas dataframe
    """
    IP_LIST = ip_dataframe.values.tolist()
    print(f"converted {len(IP_LIST)} ip_addresses")

    return IP_LIST

def main():
    from ip_to_coordinate_converter import ip_to_coord
    from locator import point_extractor, coordinate_locator
    from mapper import geo_mapping
    from query_database import failed_logins
    
    QUERY_RESULT = failed_logins()
    ip_dataframe = ip_from_query(QUERY_RESULT)
    IP_LIST = df_to_list(ip_dataframe)
    print(IP_LIST)
    raw_coordinates = ip_to_coord(IP_LIST)
    LOCATIONS = [coordinate_locator(c) for c in raw_coordinates]
    COORDINATES = point_extractor(LOCATIONS)
    geo_mapping(COORDINATES)

if __name__ == "__main__":
    main()
