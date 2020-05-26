from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt


def make_hist(obj_name, filepath, min_e, max_e, nbins='auto', i=None):
    evt_data = fits.getdata(filepath)
    energy = evt_data["PI"]
    min_thresh = evt_data["PI"] >= min_e
    max_thresh = evt_data["PI"] < max_e
    e_band = energy[min_thresh & max_thresh]
    plt.hist(e_band, bins=nbins)
    plt.title(
        f"Energy Distribution for {obj_name} between {min_e} and {max_e} eV")
    plt.xlabel("Energy (eV)")
    plt.ylabel("Count")
    plt.show()
    # plt.savefig(f"{obj_name}_ehist_{min_e}-{max_e}eV", dpi=250, format="png")
    # plt.close()
