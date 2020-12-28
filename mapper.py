import webbrowser
import time
import folium
import os

# from folium.plugins import MarkerCluster # How to use


"""
TODO
- locate_addresses() and raw_location() should be in a separete module, and mapper.py
be strictly for mapping!
"""

def render_map():
    """Render map on browser after creation in geo_mapping()"""
    cwd = os.getcwd()
    url = 'file://' + cwd + '/Maps/map.html'
    ff_path = '/usr/bin/firefox'
    webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(ff_path))
    ff = webbrowser.get(using='firefox')
    ff = webbrowser.get()
    ff.open(url, new=0, autoraise=True)
    print("Loading map...")
    time.sleep(5)

def geo_mapping(COORDINATES):
    """Map COORDINATES and save to html file
    TODO:
    - fix zoom_start value based on event?;{'event':zoom_value}
    """
    m = folium.Map(
        tiles='CartoDB dark_matter',
    )

    for point in COORDINATES:
        folium.Map(
            location=[point.latitude, point.longitude],
        ).add_to(m)

        folium.CircleMarker(
            location=[point.latitude, point.longitude],
            radius=25,
            color='#1fff96',
            fill=False,
            fill_color='#7de8b5'
        ).add_to(m)
        print(point.latitude, point.longitude)

        time.sleep(2)
    bounds = m.get_bounds()
    m.fit_bounds(bounds, padding=(20,20))
    m.save('./Maps/map.html')

    render_map() # Function to render map on browser

def main():
    
    ADDR = [
        "Tagum Philippines",
        "Davao Philippines",
        "Isabela Philippines",
        "Surigao Philippines"
    ]

    LOCATIONS = locate_addresses(ADDR)
    COORDINATES = raw_location(LOCATIONS)
    geo_mapping(COORDINATES)
    time.sleep(5)
    print("Done.")

if __name__ == "__main__":
    main()

