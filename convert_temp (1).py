import rasterio
import pandas as pd
import numpy as np

# 1) Open GRIB with rasterio
try:
    with rasterio.open("dewpoint2m_lyon7_2018.grib") as src:
        # Read metadata
        data = src.read(1)  # Read first band
        profile = src.profile
        
        # Get coordinates
        bounds = src.bounds
        width, height = src.width, src.height
        
        # Create lat/lon grids
        lons = np.linspace(bounds.left, bounds.right, width)
        lats = np.linspace(bounds.top, bounds.bottom, height)
        lon_grid, lat_grid = np.meshgrid(lons, lats)
        
        # Flatten arrays
        data_flat = data.flatten()
        lat_flat = lat_grid.flatten()
        lon_flat = lon_grid.flatten()
        
        # Create DataFrame
        df = pd.DataFrame({
            'latitude': lat_flat,
            'longitude': lon_flat,
            'd2m': data_flat
        })
        
        # Remove NaN values
        df = df.dropna()
        
        # 2) Kelvin -> Celsius
        df["Td2m_C"] = df["d2m"] - 273.15
        
        # 3) Save to CSV
        df.to_csv("dewpoint_lyon7_2018.csv", index=False)
        
        print("✅ CSV saved: dewpoint_lyon7_2018.csv")
        print("Columns:", list(df.columns))
        print(df.head())
        print(f"Total rows: {len(df)}")

except Exception as e:
    print(f"❌ Erreur: {e}")
    print("\nAlternative: vérifie que le fichier GRIB existe et essaie avec gdal")
    import sys
    sys.exit(1)
