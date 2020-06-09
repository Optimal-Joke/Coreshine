from classes import Telescope, Chandra, XMM, Swift, Rosat
import numpy as np

data_dir = "/Users/hunterholland/Documents/Research/Laidlaw/Modified Data"

chandra_sample = f"{data_dir}/L1517/Chandra/primary/acisf03755N004_evt2.fits"
xmm_sample = f"{data_dir}/L1517/XMM/PPS/P0101440801M1S001MIEVLI0000.FTZ"
rosat_sample = f"{data_dir}/L1517/ROSAT/rp201278a01_bas.fits"
swift_sample = f"{data_dir}/L1517/Swift/xrt/event/sw00034249004xpcw3po_cl.evt.gz"

# xmm = XMM(xmm_sample)
# e_region = xmm.coord_mask(24500, 24600, size_RA=4500,
#                           size_Dec=4500, newfile=True, filename="test.fits")

# testxmm = XMM(f"{data_dir}/L1517/XMM/PPS/test.fits")
# testxmm.e_hist([1000, 6000], nbins=100)
# xmm.e_mask([600, 3000], filename="test2.fits", newfile=True)
# testxmm.e_mask([600, 2000], filename="test2.fits", newfile=True)
# testxmm.e_mask([600, 1000], filename="test3.fits", newfile=True)
# testxmm.e_mask([600, 1000], filename="test4.fits", newfile=True)

# rosat = Rosat(rosat_sample)
# rosat.coord_mask(7882.0363, 6126.3879, size_RA=2377.7274,
#                  size_Dec=2350.0797, newfile=True, filename="test.fits")

swift = Swift(swift_sample)
swift.coord_mask(381.0884, 450.21112, size_RA=504.33036,
                 size_Dec=498.46605, newfile=True, filename="test2.fits")
