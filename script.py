from classes import Telescope, Chandra, XMM
import numpy as np

data_dir = "/Users/hunterholland/Documents/Research/Laidlaw/Modified Data"

test = f"{data_dir}/L1517/test.fits"
test1 = f"{data_dir}/L1517/test1.fits"

chandra_sample = f"{data_dir}/L1517/Chandra/primary/acisf03755N004_evt2.fits"

xmm_sample = f"{data_dir}/B59/XMM/PPS/P0206610101PNS003PIEVLI0000.FTZ"

# sample = Chandra(chandra_sample)
# sample.e_mask([600, 2000], [4000, 6000], newfile=True, filename="test.fits")
# sample.e_mask([6000, 10000], [14000], newfile=True, filename="test1.fits")

test = Chandra(test)
test1 = Chandra(test1)

test.e_hist(object="L1517", nbins=200, save=True)
test1.e_hist(nbins=200, save=True)
