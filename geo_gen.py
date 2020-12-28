import random

def generate_coordinates(LAT_MIN, LAT_MAX, LON_MIN, LON_MAX, PRECISION=4):
    """Generate random latitude, longitude

    Parameters
    ----------   
    LAT_MIN : Min latitude value
    LAT_MAX : Max latitiude value
    LON_MIN : Min longitude value
    LON_MAX : Max longitude value
    
    PRECISION : Decimal places for COORDINATES. Defaults to 4
    to avoid missing actual geographic location from random choices
    
    Example
    -------
    LAT_MIN = 50.9113[186]
    LAT_MAX = 50.9002[263]
    LON_MIN = -114.1263[383]
    LON_MAX = -114.0992[887]

    TODO:
    - set parameter for number COORDINATES to generate
    """
    
    lat_x = round(random.uniform(LAT_MIN, LAT_MAX), PRECISION)
    lon_x = round(random.uniform(LON_MIN, LON_MAX), PRECISION)

    return lat_x, lon_x