import pandas as pd
import matplotlib.pyplot as plt

# ===============================
# LOAD CSV
# ===============================
df = pd.read_csv("lyon7_2018.csv")

# Si ton CSV a une colonne "time" (souvent le cas)
# On la convertit en datetime pour pouvoir tracer correctement
df["time"] = pd.to_datetime(df["time"])

# ===============================
# AREA MEAN TIME SERIES
# ===============================
# Moyenne sur l’espace (lat/lon) pour chaque timestamp
ts = df.groupby("time")[["BHI", "BNI", "DHI", "GHI"]].mean()

# ===============================
# PLOT
# ===============================
plt.figure(figsize=(10, 4))
plt.plot(ts.index, ts["GHI"], label="GHI")
plt.plot(ts.index, ts["BNI"], label="BNI (DNI)")
plt.plot(ts.index, ts["DHI"], label="DHI")
plt.plot(ts.index, ts["BHI"], label="BHI")

plt.title("Area-mean irradiance time series (Lyon region) – July 2018 (clear-sky)")
plt.xlabel("Time")
plt.ylabel("Irradiance")
plt.legend()
plt.tight_layout()

plt.savefig("timeseries_lyon7_2018.png", dpi=200)
plt.show()

print("✅ Figure saved: timeseries_lyon7_2018.png")
