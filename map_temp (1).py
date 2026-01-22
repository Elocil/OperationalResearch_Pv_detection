import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load
df = pd.read_csv("dewpoint_lyon7_2018.csv")

# Grid (mean per cell)
m = df.groupby(["latitude", "longitude"])["Td2m_C"].mean().reset_index()
grid = m.pivot(index="latitude", columns="longitude", values="Td2m_C")
grid = grid.sort_index(axis=0).sort_index(axis=1)

lats = grid.index.to_numpy()
lons = grid.columns.to_numpy()
Z = grid.to_numpy()

# Plot heatmap
fig, ax = plt.subplots(figsize=(7, 6))
im = ax.imshow(
    Z,
    origin="lower",
    aspect="auto",
    extent=[lons.min(), lons.max(), lats.min(), lats.max()]
)

cbar = plt.colorbar(im, ax=ax)
cbar.set_label("Mean 2m dewpoint (°C)")

ax.set_title("Mean 2m dewpoint – July 2018 (Lyon region)")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

# Annotate each cell with value
nrows, ncols = Z.shape

# Compute cell centers from extent (works even if 2x2)
x_edges = np.linspace(lons.min(), lons.max(), ncols + 1)
y_edges = np.linspace(lats.min(), lats.max(), nrows + 1)
x_centers = (x_edges[:-1] + x_edges[1:]) / 2
y_centers = (y_edges[:-1] + y_edges[1:]) / 2

for i, y in enumerate(y_centers):
    for j, x in enumerate(x_centers):
        val = Z[i, j]
        if np.isfinite(val):
            ax.text(x, y, f"{val:.2f}", ha="center", va="center", fontsize=11)

plt.tight_layout()
plt.savefig("map_dewpoint_lyon7_2018_annotated.png", dpi=200)
plt.show()

print("✅ Saved: map_dewpoint_lyon7_2018_annotated.png")
