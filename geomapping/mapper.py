import webbrowser
import time
import folium
import os


from geomapping.locator import address_locator, point_extractor

def render_map():
    """Render map on browser after creation in geo_mapping()"""
    cwd = os.getcwd()
    url = 'file://' + cwd + '/geomapping/maps/map.html'
    ff_path = '/usr/bin/firefox'
    webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(ff_path))
    ff = webbrowser.get(using='firefox')
    ff = webbrowser.get()
    ff.open(url, new=0, autoraise=True)
    print("Loading map...")
    time.sleep(2)

def geo_mapping(COORDINATES):
    """Map COORDINATES and save to html file
    Parameters
    ----------
    COORDINATES : [(LATITUDE, LONGITUDE)]
    List of <class 'geopy.location.Location'>
    
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
    
    print("Mapping coordinates... ")
    
    for point in COORDINATES:
        folium.Map(
            location=[point.latitude, point.longitude],
        ).add_to(m)

        folium.CircleMarker(
            location=[point.latitude, point.longitude],
            radius=10,
            color='#1fff96',
            fill=False,
            fill_color='#7de8b5'
        ).add_to(m)

    bounds = m.get_bounds()
    m.fit_bounds(bounds, padding=(20,20))
    print(os.getcwd())
    m.save('./geomapping/maps/map.html')

    render_map() # Function to render map on browser

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
    geo_mapping(COORDINATES)
    time.sleep(5)
    print("Done.")

if __name__ == "__main__":
    main()