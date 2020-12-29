from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


GEOLOCATOR = Nominatim(user_agent="TestMapper")
geocode = RateLimiter(GEOLOCATOR.geocode, min_delay_seconds=2)

def lookup_coordinates(ADDR):
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

def raw_location(LOCATIONS):
    """Get the raw COORDINATES off LOCATIONS
    
    Parameters
    ----------
    LOCATIONS : <class 'geopy.location.Location'>
    """    
    COORDINATES = [location.point for location in LOCATIONS]
    return COORDINATES