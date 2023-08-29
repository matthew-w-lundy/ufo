import numpy as np
import astropy.units as u

# %matplotlib inline
import matplotlib.pyplot as plt
from IPython.display import display
from gammapy.catalog import CATALOG_REGISTRY

from gammapy.catalog import SourceCatalog4FGL
from gammapy.modeling.models import create_crab_spectral_model

fluxes=np.genfromtxt('fluxes.txt')
sources=np.genfromtxt('sources.txt',dtype=None,delimiter=',')


catalog = SourceCatalog4FGL()


for source in sources:
    s=source.decode("utf-8")
    print(catalog[s].associations)