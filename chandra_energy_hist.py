import glob
from astropy.io import fits
from data_functions import make_hist


data_dir = "/Users/hunterholland/Documents/Research/Laidlaw/Data"

chandra_evt2_files = glob.glob(
    f"{data_dir}/**/Chandra/**/*evt2.fits", recursive=True)


i = 1
for file in chandra_evt2_files:
    make_hist(file, 100, 500, i=i)
    i += 1
