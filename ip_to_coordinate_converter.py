from ip2geotools.databases.noncommercial import DbIpCity
from ip2geotools.errors import ServiceError
from ip2geotools.errors import InvalidRequestError

def ip_to_coord(IP_LIST):
    """Convert IP_LIST to COORDINATES
    TODO:
    - create KeyError counter? Or limit accuracy of COORDINATES?
    - pickle batch conversion
    """
    COORDINATES = set() # no duplicate coordinate.
    error_counter = 0
    print(f"Converting {len(IP_LIST)} to COORDINATES")
    for ip in IP_LIST[:5]:
        try:
            response = DbIpCity.get(ip, api_key='free') # DbIpCity ServiceError?
            c = (response.latitude, response.longitude)
            COORDINATES.add(c)
            print(f"{ip} ---> ({response.latitude},{response.longitude})")
            # time.sleep(1)
        except KeyError as err:
            print(err)
            error_counter += 1
            pass
        except ServiceError as err:
            print(err)
            error_counter += 1
            pass
        except InvalidRequestError as err:
            print(err)
            error_counter += 1
            pass
    print(f"Processing {len(COORDINATES)} COORDINATES. Duplicates removed.")
    print(f"{error_counter} errors encountered.")
    return COORDINATES

def main(IP_LIST):
    """Convert IP_LIST to COORDINATES"""
    import query_database 
    IP_LIST = query_database
    COORDINATES = ip_to_coord(IP_LIST)

    return COORDINATES

if __name__ == "__main__":
    main()