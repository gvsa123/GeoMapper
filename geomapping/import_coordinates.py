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
    """Takes the result of query_database and converts to df of ip_address
    Result
    ------
    IP_LIST : list of ip_addresses
    """
    ip_dataframe = pd.DataFrame(
        QUERY_RESULT,
        columns=['id', 'user_id', 'user_login', 'failed_login_date', 'login_attempt_ip']    
    )

    ip_dataframe.drop_duplicates(subset='login_attempt_ip', inplace=True)
    ip_dataframe = pd.Series(ip_dataframe['login_attempt_ip'])

    print("Duplicates removed.\n")

    return ip_dataframe

def df_to_list(ip_dataframe):
    """Convert ip_dataframe to list of ip addresses
    Parameters
    ----------
    ip_dataframe : pandas dataframe
    """
    
    IP_LIST = [ip for ip in ip_dataframe]    
    print(f"{len(IP_LIST)} ip_addresses in IP_LIST\n")

    return IP_LIST

def main():
    from ip_converter import ip_to_coord
    from locator import point_extractor, coordinate_locator
    from query_database import failed_logins
    
    QUERY_RESULT = failed_logins()
    ip_dataframe = ip_from_query(QUERY_RESULT)
    IP_LIST = df_to_list(ip_dataframe)
    print(IP_LIST)

if __name__ == "__main__":
    main()
