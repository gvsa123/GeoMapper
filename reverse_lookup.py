from locator import *
from geo_gen import generate_coordinates

def reverse_lookup(COORDINATES):
    """Look up LOCATIONS based on COORDINATES

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
        35.689831, 51.434823, 36.688983, 48.471208
        ) for x in range(10)
    ]
    print(COORDINATES)

    test = [reverse_lookup(x) for x in COORDINATES]

    geo_mapping(test)

if __name__ == "__main__":
    main()