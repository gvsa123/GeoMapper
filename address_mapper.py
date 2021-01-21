def main():
    """Convert IP_LIST to COORDINATESformat"""

    from geomapping.ip_converter import remaining_queries
    
    print("Running daily quota check.")
    url = 'http://api.db-ip.com/v2/free'
    limit = remaining_queries(URL=url)
    print("Daily quota left : {}".format(limit))

    from geomapping.query_database import failed_logins
    from geomapping.import_coordinates import ip_from_query, df_to_list
    from geomapping.ip_converter import json_parser, batch_query

    # Extract ip addresses from database
    QUERY_RESULT = failed_logins()
    ip_dataframe = ip_from_query(QUERY_RESULT)
    IP_LIST = df_to_list(ip_dataframe)
    
    assert limit > len(IP_LIST), 'Daily quota limit not enough.'
    
    json_data = batch_query(IP_LIST=IP_LIST[:32], URL=url) # Limit to 32 while split_query() not complete

    ADDR = json_parser(json_data)

    from geomapping.locator import address_locator
    from geomapping.mapper import geo_mapping

    address = address_locator(ADDR)
    geo_mapping(address)



    # COORDINATES = ip_to_coord(IP_LIST, query)

    # return COORDINATES

if __name__ == "__main__":
    main()