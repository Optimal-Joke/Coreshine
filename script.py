from classes import Telescope, Chandra, XMM, Swift, Rosat
import numpy as np
import glob

data_dir = "/Users/hunterholland/Documents/Research/Laidlaw/Data/Modified"

chandra_sample = f"{data_dir}/L1517/Chandra/primary/acisf03755N004_evt2.fits"
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

# swift = Swift(cleaned_event[0])
# energies = swift.coord_mask(
#     446.90694, 487.76449, size_RA=137.97797, size_Dec=139.31756)
# energies = swift.e_mask(newfile=False, filename="cl_evt_f1.fits")
# swift.e_hist(e_list=energies, nbins=150)


# for file in pn:
#     xmm = XMM(file)
#     xmm.e_mask([0,12000], newfile=True, filename="PN_PIEVLI_f1.fits")

xmm_object = XMM(
    "/Users/hunterholland/Documents/Research/Laidlaw/Data/Modified/L1517/XMM/PPS/evt/P0109270401M1S001MIEVLI0000.ftz")
xmm_object.e_mask([600, 1500], newfile=True, filename="test.fits")
# xmm_object.e_hist(e_list=energies)
