def make_cyclic_and_shiftgrid(array, lons):
        import numpy as np
        temp1, templons = addcyclic(array, lons)
        temp2= shiftgrid(180., temp1, templons, start=False)
        return temp2
