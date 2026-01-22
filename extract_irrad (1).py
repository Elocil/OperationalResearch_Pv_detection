import cdsapi
import xarray as xr
import pandas as pd

# ===============================
# DOWNLOAD CAMS SOLAR DATA
# ===============================

dataset = "cams-gridded-solar-radiation"

request = {
    "variable": [
        "global_horizontal_irradiation",
        "direct_horizontal_irradiation",
        "diffuse_horizontal_irradiation",
        "direct_normal_irradiation"
    ],
    "sky_type": ["clear"],
    "version": ["4.5"],
    "year": ["2018"],
    "month": ["07"],                 # UN SEUL MOIS
    "area": [46.3, 4.7, 45.4, 6.1]   # Lyon–Grenoble–Chambéry (réduit)
}
client = cdsapi.Client(
    url="https://ads.atmosphere.copernicus.eu/api",
    key="f1a97451-0516-43da-90b3-0966dd4337df",
    verify=False
)

client.retrieve(dataset, request).download()