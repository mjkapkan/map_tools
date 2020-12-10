# author: mjkapkan
# requirements pyproj v2 (pip install pyproj)

from pyproj import Transformer

def convert_lks94(x,y):     # Converts LKS-94 x,y coordinates to Latitude and Longitude
                            # as described in https://spatialreference.org/ref/epsg/3346/
                            # LKS-94 Lithuanian: (Lietuvos Koordinačių Sistema, priimta 1994 m.)
    transproj = Transformer.from_crs(
        "epsg:3346",
        "epsg:4326",
        always_xy=True
    )

    lon, lat = transproj.transform(
        x,
        y,
    )
    return lat,lon

#### Example:
## lat,lon = convert_lks94(529234.0,6221055.0)
## print(f"{lat}, {lon}")
