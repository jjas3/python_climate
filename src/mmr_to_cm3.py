#!/usr/bin/env/python
def mmr_to_number_den_in_cm3 (press, temp, MMR, RMM_in_g_mol):
    """
    return number density in cm3
    pressure in Pa
    Temp in K
    MMR in kg per kg
    RMM in g per mol
    """
    return (28.8/RMM_in_g_mol)*(press/(8.31*temp))*MMR/1e6*6.02e23
