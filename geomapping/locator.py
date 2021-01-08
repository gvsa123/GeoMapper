from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

GEOLOCATOR = Nominatim(user_agent="TestMapper")
geocode = RateLimiter(GEOLOCATOR.geocode, min_delay_seconds=2)

def address_locator(ADDR):
    """Returns address as a geopy object
    
    Parameters
    ----------
    ADDR : ["NUMBER STREET CITY COUNTRY"]
    
    Returns
    -------
    addresses : list <class 'geopy.location.Location'>
    """
    addresses = [GEOLOCATOR.geocode(address) for address in ADDR]
    
    return addresses

def point_extractor(LOCATIONS):
    """Get POINTS from LOCATIONS
    
    Parameters
    ----------
    LOCATIONS : <class 'geopy.location.Location'>
    """    
    COORDINATES = [location.point for location in LOCATIONS]
    return COORDINATES

def coordinate_locator(COORDINATES):
    """Look up COORDINATES and convert to geopy.location
    
    Parameters
    ----------
    COORDINATES : [(LATITUDE, LONGITUDE)] or string as "%(latitude)s, %(longitude)s"
    (see documentation)

    Returns
    -------
    <class 'geopy.location.Location'>
    """

    addresses = GEOLOCATOR.reverse(COORDINATES)
    return addresses
