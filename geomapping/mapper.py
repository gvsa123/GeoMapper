import webbrowser
import time
import folium
from os.path import expanduser


from geomapping.locator import address_locator, point_extractor

def render_map():
    """Render map on browser after creation in geo_mapping()"""
    home = expanduser('~')
    url = 'file://' + home + '/Scripts/Python/geomapping/app/templates/map.html'
    ff_path = '/usr/bin/firefox'
    webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(ff_path))
    ff = webbrowser.get(using='firefox')
    ff = webbrowser.get()
    ff.open(url, new=0, autoraise=True)
    print("loading map")
    time.sleep(2)

def geo_mapping(COORDINATES, no_browser=0):
    """Map COORDINATES and save to html file
    Parameters
    ----------
    COORDINATES : [(LATITUDE, LONGITUDE)]
    List of <class 'geopy.location.Location'>

    no_browser : open map in browser
    
    Example
    -------
    [Location(Цагаан-Овоо, Дорнод, Монгол улс ᠮᠤᠩᠭᠤᠯ ᠤᠯᠤᠰ, (48.456334749999996, 113.16934292655316, 0.0)),
    Location(Баяндун, Дорнод, Монгол улс ᠮᠤᠩᠭᠤᠯ ᠤᠯᠤᠰ, (49.3767858, 113.29484344645006, 0.0)),
    Location(Цагаан-Овоо, Дорнод, Монгол улс ᠮᠤᠩᠭᠤᠯ ᠤᠯᠤᠰ, (48.456334749999996, 113.16934292655316, 0.0)),
    Location(Баяндун, Дорнод, Монгол улс ᠮᠤᠩᠭᠤᠯ ᠤᠯᠤᠰ, (49.3767858, 113.29484344645006, 0.0)),
    Location(Сэргэлэн, Дорнод, Монгол улс ᠮᠤᠩᠭᠤᠯ ᠤᠯᠤᠰ, (48.6156235, 114.10796309205668, 0.0))]
    
    TODO:
    - check for duplicate/proximal coordinates
    """

    m = folium.Map(
        tiles='CartoDB dark_matter',
    )
    
    print("mapping coordinates ")
<<<<<<< HEAD
    try:
        for point in COORDINATES:
            print(
                point
            )
=======
    
    for point in COORDINATES:
        try:
>>>>>>> flaskdev
            folium.Marker(
                location=[point.latitude, point.longitude],
                icon=None
            )#.add_to(m)

            folium.CircleMarker(
                location=[point.latitude, point.longitude],
                radius=10,
                color='#1fff96',
                fill=False,
                fill_color='#7de8b5'
            ).add_to(m)
<<<<<<< HEAD
    except AttributeError as e:
        pass
=======
        except AttributeError as e:
            print(e)
>>>>>>> flaskdev

    bounds = m.get_bounds()
    m.fit_bounds(bounds, padding=(20,20))
    m.save('./app/templates/map.html')

    if no_browser == 1:
        render_map() # render map in browser

def main():
    
    print("Generating sample.")
    ADDR = [
        "Tagum Philippines",
        "Davao Philippines",
        "Isabela Philippines",
        "Surigao Philippines",
        "Marikina Philippines"
    ]

    LOCATIONS = address_locator(ADDR)
    COORDINATES = point_extractor(LOCATIONS)
    geo_mapping(COORDINATES, no_browser=0)
    time.sleep(5)
    print("Done.")

if __name__ == "__main__":
    main()