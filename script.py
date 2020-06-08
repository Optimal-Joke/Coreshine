from classes import Telescope, Chandra, XMM
import numpy as np

data_dir = "/Users/hunterholland/Documents/Research/Laidlaw/Modified Data"

test = f"{data_dir}/L1517/test.fits"
test1 = f"{data_dir}/L1517/test1.fits"

chandra_sample = f"{data_dir}/L1517/Chandra/primary/acisf03755N004_evt2.fits"

xmm_sample = f"{data_dir}/B59/XMM/PPS/P0206610101PNS003PIEVLI0000.FTZ"

chandra = Chandra(chandra_sample)
chandra2 = Chandra(
    "/Users/hunterholland/Documents/Research/Laidlaw/Modified Data/L1448/Chandra/primary/acisf04497N003_evt2.fits")

# print(chandra.e_mask())
# print(chandra.coord_mask(6000, 6000, size_RA=100, size_Dec=100, save=True))
energies = chandra.e_mask()
energies2 = chandra2.e_mask()

chandra.e_hist(e_list=energies, e_list2=energies2, object="L1448 & L1517")

# xmm = XMM(xmm_sample)
# print(xmm.file_dir)
