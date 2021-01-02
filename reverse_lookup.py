from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from geo_gen import generate_coordinates
from locator import coordinate_locator
from mapper import geo_mapping

GEOLOCATOR = Nominatim(user_agent="TestMapper")
geocode = RateLimiter(GEOLOCATOR.geocode, min_delay_seconds=2)

def main(COORDINATES):
    """
    create test_geo_gen.py and test_geo_gen.py
    raise TypeError("`address` must not be None")
    TypeError: `address` must not be None
    """
    test = []
    for x in COORDINATES:
        print("x = {}".format(x))
        y = coordinate_locator(x)
        test.append(y)
        print("y = {}".format(y))

    # test = [coordinate_locator(x) for x in COORDINATES] # Move to test
 
    geo_mapping(test)

if __name__ == "__main__":
    COORDINATES = [
        generate_coordinates(
        48.1701,49.2789,-112.4616,-113.9444,
        PRECISION=6) for x in range(5)
    ]
    print(COORDINATES)
    main(COORDINATES)