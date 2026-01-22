import xarray as xr
import pandas as pd

ds_BHI = xr.open_dataset('data_cams_2018_07/v4.5_BHI_clear_2018_07.area-subset.46.3.6.1.45.4.4.7.nc', engine='h5netcdf')
ds_BNI = xr.open_dataset('data_cams_2018_07/v4.5_BNI_clear_2018_07.area-subset.46.3.6.1.45.4.4.7.nc', engine='h5netcdf')
ds_DHI = xr.open_dataset('data_cams_2018_07/v4.5_DHI_clear_2018_07.area-subset.46.3.6.1.45.4.4.7.nc', engine='h5netcdf')
ds_GHI = xr.open_dataset('data_cams_2018_07/v4.5_GHI_clear_2018_07.area-subset.46.3.6.1.45.4.4.7.nc', engine='h5netcdf')

df_converted_BHI = ds_BHI.to_dataframe()
df_converted_BNI = ds_BNI.to_dataframe()
df_converted_DHI = ds_DHI.to_dataframe()
df_converted_GHI = ds_GHI.to_dataframe()

df_combined = pd.concat([df_converted_BHI, df_converted_BNI, df_converted_DHI, df_converted_GHI], axis=1)
df_combined.columns = ['BHI', 'BNI', 'DHI', 'GHI']

df_combined.to_csv('lyon7_2018.csv', index=True)
print('Dataset converted to DataFrame and saved to output_data_irradiance.csv')
