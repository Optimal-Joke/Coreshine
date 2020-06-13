from classes import Telescope, Chandra, XMM, Swift, Rosat
import numpy as np

data_dir = "/Users/hunterholland/Documents/Research/Laidlaw/Data/Modified"

chandra_sample = f"{data_dir}/L1517/Chandra/primary/acisf03755N004_evt2.fits"
xmm_sample = f"{data_dir}/L1517/XMM/PPS/evt/P0101440801M1S001MIEVLI0000.FTZ"
rosat_sample = f"{data_dir}/L1517/ROSAT/rp201278a01_bas.fits.Z"
swift_sample = f"{data_dir}/L1517/Swift/xrt/event/sw00034249004xpcw3po_cl.evt.gz"

# chandra = Chandra(chandra_sample)
# energies = chandra.coord_mask(
#     4113.5, 4095.5, size_RA=81, size_Dec=107, newfile=True, filename="test.fits")
# chandra.e_mask([600, 4000], newfile=True, filename="evt2_f2.fits")
# chandra.e_hist([1000, 2000], [3000, 4000], nbins=200)

xmm = XMM(xmm_sample)
xmm.e_mask([600, 3000], newfile=True, filename="M1_f1.fits")
# xmm.coord_mask(
#     24424.714, 24595.563, size_RA=797.04012, size_Dec=1052.8802, newfile=True, filename="test1.fits")
# xmm.e_hist([600, 1000], [2000], nbins=200)

# rosat = Rosat(rosat_sample)
# energies = rosat.e_mask([50, 100], [200])
# rosat.e_hist(e_list=energies)

# swift = Swift(swift_sample)
# energies = swift.coord_mask(
#     532.43458, 501.10731, size_RA=168.60103, size_Dec=162.92732, newfile=True, filename="test.fits")
# swift.e_hist([20, 100], [150], nbins=100)
