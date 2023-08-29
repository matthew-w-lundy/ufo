import numpy as np
import astropy.units as u

# %matplotlib inline
import matplotlib.pyplot as plt
from IPython.display import display
from gammapy.catalog import CATALOG_REGISTRY

from gammapy.catalog import SourceCatalog4FGL
from gammapy.modeling.models import create_crab_spectral_model



catalog = SourceCatalog4FGL()
i=-1
sourceList=[]
fluxList=[]

emin=300
emax=10
crab = create_crab_spectral_model('hess_ecpl')
crab=crab.integral(emin * u.GeV,  emax* u.TeV)



for source in catalog:


    try:
        fermisource_spec=source.spectral_model()
        fermisource_sky=source.sky_model().spatial_model
        hour=(fermisource_sky.lon_0.value/360)*24
    except:
        pass
    if (hour>8) & (hour<10):
        if fermisource_sky.lat_0.value >-13:
            try:
                flux=(fermisource_spec.integral(energy_min=emin * u.GeV, energy_max=emax * u.TeV)/crab).to('%').value

                fermisource_spec.plot(energy_bounds=[0.05, 300] * u.GeV,energy_power=2)
                source.flux_points.plot(sed_type="e2dnde")
            except:
                pass
            if flux >1:
            
                sourceList.append(source.name)
                print(flux)
                fluxList.append(flux)
        if hour>10:
            break
        else:
            print('fail')
np.savetxt('sources.txt',sourceList,fmt='%s')
np.savetxt('fluxes.txt',fluxList,fmt='%s')

plt.show()