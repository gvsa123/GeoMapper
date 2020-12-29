import random

def generate_coordinates(LAT_MIN, LAT_MAX, LON_MIN, LON_MAX, PRECISION=6):
    """Generate random latitude, longitude

    Parameters
    ----------   
    LAT_MIN : Min latitude value
    LAT_MAX : Max latitiude value
    LON_MIN : Min longitude value
    LON_MAX : Max longitude value
    
    PRECISION : Default decimal places for COORDINATES.
    
    Example
    -------
    LAT_MIN = 50.9113
    LAT_MAX = 50.9002
    LON_MIN = -114.1263
    LON_MAX = -114.0992

    TODO:
    - set parameter for number COORDINATES to generate
    """
    
    lat_x = round(random.uniform(LAT_MIN, LAT_MAX), PRECISION)
    lon_x = round(random.uniform(LON_MIN, LON_MAX), PRECISION)

    return lat_x, lon_x