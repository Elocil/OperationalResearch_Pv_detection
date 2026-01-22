# OperationalResearch

This repository contains **two independent projects**:

1. **Georeferenced Irradiance & Temperature Analysis (Lyon region) — July 2018**
2. **Photovoltaic Panel Detection using YOLOv8**

---

# 1) Georeferenced Irradiance & Temperature Analysis (Lyon region) — July 2018

This project provides a reproducible Python workflow to **download**, **process**, and **visualize** georeferenced **solar irradiance** and **near-surface atmospheric moisture (2m dewpoint temperature)** over a small region around **Lyon–Grenoble–Chambéry**, for **July 2018**.

## Data sources (Copernicus Atmosphere Data Store — ADS)

- **CAMS gridded solar radiation** (irradiance components: GHI, BHI, DHI, BNI/DNI)
- **CAMS global reanalysis EAC4 monthly** (2m dewpoint temperature, monthly mean)

## Scripts (what each one does)

### Irradiance (CAMS solar)
- `extract_irrad.py` — downloads CAMS irradiance for the study area (ZIP output)
- `unzip.py` — extracts the downloaded ZIP into a local folder
- `conversion_irrad.py` — converts NetCDF files to a single merged CSV (`lyon7_2018.csv`)
- `times_series.py` — produces an **area-mean** irradiance time series plot
- `cartographic_heatmap.py` — produces a **cartographic heatmap** (mean GHI) over an OSM basemap

### Temperature / moisture (EAC4 monthly)
- `extract_temp.py` — downloads EAC4 monthly 2m dewpoint temperature (GRIB)
- `convert_temp.py` — converts GRIB to CSV (`dewpoint_lyon7_2018.csv`) and Kelvin → °C
- `map_temp.py` — heat map of dewpoint with **annotated mean values** per grid cell

> Note: the EAC4 monthly dataset can have a **coarse spatial resolution** over a small domain.  
> In that case, only a few grid cells are available; annotating values improves transparency and interpretation.

## Study area (bounding box)

All downloads use the same bounding box: **[North, West, South, East]**

```txt
North = 46.3
West  = 4.7
South = 45.4
East  = 6.1
