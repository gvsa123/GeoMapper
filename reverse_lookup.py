from locator import *
from geo_gen import generate_coordinates
from mapper import geo_mapping

def lookup_coordinates(COORDINATES):
    """Look up COORDINATES and convert to geopy.location

    Parameters
    ----------
    COORDINATES : [(LATITUDE, LONGITUDE)]

    Returns
    -------
    <class 'geopy.location.Location'>
    """

    addresses = GEOLOCATOR.reverse(COORDINATES)
    return addresses

def main():
    
    COORDINATES = [
        generate_coordinates(
        50.278923, 3.944454, 51.170177, 10.461686,
        PRECISION=6) for x in range(10)
    ]
    print(COORDINATES)
    """
    create test_geo_gen.py and test_geo_gen.py
    raise TypeError("`address` must not be None")
    TypeError: `address` must not be None
    """
    test = [lookup_coordinates(x) for x in COORDINATES]

    geo_mapping(test)

if __name__ == "__main__":
    main()