import zipfile
from pathlib import Path

zip_path = Path("lyonjuillet.zip")
out_dir = Path("data_cams_2018_07")
out_dir.mkdir(exist_ok=True)

with zipfile.ZipFile(zip_path, "r") as z:
    z.extractall(out_dir)

print("Extraction terminée ✅")
