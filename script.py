from classes import Chandra, XMM

data_dir = "/Users/hunterholland/Documents/Research/Laidlaw/Modified Data"

chandra_sample = f"{data_dir}/L1517/Chandra/primary/acisf03755N004_evt2.fits"

xmm_sample = f"{data_dir}/B59/XMM/PPS/P0206610101PNS003PIEVLI0000.FTZ"

instance = XMM("P0206610101PNS003PIEVLI0000.FTZ")

energy = instance.e_mask(6000, 10000)
instance.e_hist(e_list=energy)
