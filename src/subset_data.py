def subset_3d_array (dataset, lat, lat_range, lon, lon_range):
    """
    take a 3D data field and do a zonal mean, i.e. across a latitude circle,
    over a given lat range
    i.e. zonal mean of 20S-20N datc
    """
    import numpy as np
    lat_min = lat_range[0]
    lat_max = lat_range[1]
    lat_max_idx = np.abs(lat - lat_max).argmin()
    lat_min_idx = np.abs(lat - lat_min).argmin()
    lon_min = lon_range[0]
    lon_min_idx = np.abs(lon - lon_min).argmin()
    lon_max = lon_range[1]
    lon_max_idx = np.abs(lon - lon_max).argmin()
    # subset the data into the months of interest and the lat region of interest
    datasubset = dataset[:,lat_min_idx:lat_max_idx, lon_min_idx:lon_max_idx]
    # take zonal mean
    #print lat_min_idx, lat_max_idx, lon_min_idx, lon_max_idx, np.shape(datasubset)
    return lat[lat_min_idx:lat_max_idx], lon[lon_min_idx:lon_max_idx], datasubset
