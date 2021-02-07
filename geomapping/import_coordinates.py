import pandas as pd
import time

def ip_from_csv(CSV_FILE='./Data/failed_logins.csv'):
    """Import COORDINATES from csvfile. Removes duplicates.
    """

    ip_dataframe = pd.read_csv(
        CSV_FILE,
        delimiter='\t',
        names=['id', 'user_id', 'user_login', 'failed_login_date', 'login_attempt_ip'],
        usecols=['login_date', 'ip_address', 'failed_login_date']
    ).drop_duplicates(subset=['ip_address', 'failed_login_date'])
    
    return ip_dataframe

def ip_from_query(QUERY_RESULT):
    """Takes the result of query_database and converts to df of ip_address
    Result
    ------
    IP_LIST : list of ip_addresses
    """
    ip_dataframe = pd.DataFrame(
        QUERY_RESULT,
        columns=['id', 'user_id', 'user_login', 'failed_login_date', 'login_attempt_ip']    
    )

    ip_dataframe.drop_duplicates(subset=['login_attempt_ip'], inplace=True)
    ip_dataframe = ip_dataframe[['failed_login_date', 'login_attempt_ip']]
    ip_dataframe['login_attempt_ip'] = ip_dataframe['login_attempt_ip'].astype('string', copy=False)

    print("duplicates removed")

    return ip_dataframe

def df_to_list(ip_dataframe):
    """Convert ip_dataframe to list of ip addresses
    Parameters
    ----------
    ip_dataframe : pandas dataframe
    """
    
    IP_LIST = [ip for ip in ip_dataframe['login_attempt_ip']]
    
    return IP_LIST

def df_to_addr(ip_dataframe, json_data):
    """Function to map json_data keys to ip_dataframe"""
    for ip in ip_dataframe['login_attempt_ip']:
        try:
            address = "{}, {}, {}".format(json_data[ip]['city'], json_data[ip]['stateProv'], json_data[ip]['countryName'])
            ip_dataframe['located_address'] = ip_dataframe['login_attempt_ip'].map(json_data)
        except KeyError as ke:
            print("Missing: {}".format(ke))
            pass

    return ip_dataframe

def main():
    from ip_converter import ip_to_coord
    from locator import point_extractor, coordinate_locator
    from query_database import failed_logins
    
    QUERY_RESULT = failed_logins()
    ip_dataframe = ip_from_query(QUERY_RESULT)
    IP_LIST = df_to_list(ip_dataframe)
    
if __name__ == "__main__":
    main()
