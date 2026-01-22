import cdsapi

dataset = "cams-global-reanalysis-eac4-monthly"

request = {
    "variable": ["2m_dewpoint_temperature"],
    "year": ["2018"],
    "month": ["07"],
    "product_type": ["monthly_mean"],
    "data_format": "grib",
    "area": [46.3, 4.7, 45.4, 6.1]  # North, West, South, East
}

client = cdsapi.Client(
    url="https://ads.atmosphere.copernicus.eu/api",
    key="f1a97451-0516-43da-90b3-0966dd4337df",
    verify=False
)

client.retrieve(dataset, request).download("dewpoint2m_lyon7_2018.grib")
print("✅ Downloaded: dewpoint2m_lyon7_2018.grib")
