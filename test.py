from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt


def make_hist(filepath, min_e, max_e, nbins='auto', i=None):
    evt_data = fits.getdata(filepath)
    energy = evt_data["energy"]
    min_thresh = evt_data["energy"] >= min_e
    max_thresh = evt_data["energy"] < max_e
    e_band = energy[min_thresh & max_thresh]
    plt.hist(e_band, bins=nbins)
    plt.title("Test")
    plt.xlabel("Energy (eV)")
    plt.ylabel("Count")
    plt.savefig(f"energy_hist_{min_e}_{max_e}_{i}", format="png")
    plt.close()
