def run_mapper():
    """Convert IP_LIST to COORDINATESformat"""

    from geomapping.ip_converter import remaining_queries
    
    print("running daily quota check")
    url = 'http://api.db-ip.com/v2/free'
    limit = remaining_queries(URL=url)
    print(f"daily quota {limit}")

    from geomapping.query_database import failed_logins
    from geomapping.import_coordinates import ip_from_query, df_to_list, df_to_addr
    from geomapping.ip_converter import json_parser, batch_query

    # Extract ip addresses from database
    QUERY_RESULT = failed_logins()
    if len(QUERY_RESULT) != 0:
        ip_dataframe = ip_from_query(QUERY_RESULT)
        IP_LIST = df_to_list(ip_dataframe)

        assert limit > len(IP_LIST), 'Daily quota limit not enough.'
        
        json_data = batch_query(IP_LIST=IP_LIST[:31], URL=url) # Limit to 32 while split_query() not complete
       
       
       
        ADDR = json_parser(json_data) # Parsed addresses for locator; no longer needed after json_data mapping?

        ip_dataframe = df_to_addr(ip_dataframe, json_data)
        
        print(ip_dataframe)
        # print(ip_dataframe.shape)
        # print(ip_dataframe.columns)
        # Try converting ip_dataframe['login_attempt_ip] to stringDtype
        print(ADDR)






        from geomapping.locator import address_locator
        from geomapping.mapper import geo_mapping

        address = address_locator(ADDR)
        geo_mapping(address)

        return ip_dataframe
    else:
        print(f"{len(QUERY_RESULT)} failed login attempts. Exiting")

if __name__ == "__main__":
    run_mapper()