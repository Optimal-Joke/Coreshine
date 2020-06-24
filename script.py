from classes import Telescope, Chandra, XMM, Swift, Rosat
import numpy as np
import glob

data_dir = "/Users/hunterholland/Documents/Research/Laidlaw/Data/Modified"

chandra_sample = f"{data_dir}/L1517/Chandra/primary/acisf03755N004_evt2.fits.gz"
xmm_sample = f"{data_dir}/L1517/XMM/PPS/evt/P0101440801M1S001MIEVLI0000.FTZ"
rosat_sample = f"{data_dir}/L1517/ROSAT/rp201278a01_bas.fits.Z"
swift_sample = f"{data_dir}/L1517/Swift/xrt/event/sw00034249004xpcw3po_cl.evt.gz"

# Chandra
evt2 = glob.glob(f"{data_dir}/**/Chandra/**/*evt2.fits*", recursive=True)

# XMM
mos_1 = glob.glob(f"{data_dir}/**/XMM/PPS/evt/*M1*MIEVLI*.FTZ", recursive=True)
mos_2 = glob.glob(f"{data_dir}/**/XMM/PPS/evt/*M2*MIEVLI*.FTZ", recursive=True)
pn = glob.glob(f"{data_dir}/**/XMM/PPS/evt/*PN*PIEVLI*.FTZ", recursive=True)

# Rosat
basics = glob.glob(f"{data_dir}/**/ROSAT/*_bas*", recursive=True)

# Swift
cleaned_event = glob.glob(
    f"{data_dir}/**/Swift/xrt/event/sw*po_cl.evt.gz", recursive=True)

rosat = Rosat(rosat_sample)
rosat.e_hist()
