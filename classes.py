import os
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

# data_dir should be a directory containing each object as it's own subdirectory. Objects should have subdirectories for each telescope's data.
data_dir = "/Users/hunterholland/Documents/Research/Laidlaw/Modified Data"

objects = {}
# Creates dictionary of object names and their directories' file paths.
for entry in os.scandir(data_dir):
    if not entry.name.startswith('.') and entry.is_dir():
        objects[entry.name] = entry.path


class Spitzer:
    """
    """

    def e_hist(self, min_e, max_e, nbins='auto'):
        pass


class Chandra:
    """Takes a file path or name as input. As of now, this class can only initiate data, yield energy histograms, and apply energy masks.
    """

    def __init__(self, file):
        if os.path.isfile(file):  # Assign input to filepath
            self.path = file
        else:  # Get filepath from file input
            for path, _dir, files in os.walk(f"{data_dir}"):
                if file in files:
                    self.path = os.path.join(path, file)
        # Using self.path, get object name from object dictionary.
        for item in objects.keys():
            if item in self.path:
                self.objectname = item
        # Get object path from object directory.
        obj_path = objects[self.objectname]
        self.telescopes = []
        for telescope in os.scandir(obj_path):
            if telescope.is_dir() and "." not in telescope.name:
                # List telescopes with object data.
                self.telescopes.append(telescope.name)
        if not "Chandra" in self.telescopes:
            self.init_message = f"{self.objectname} has no data from Chandra telescope."
        else:
            self.init_message = "Chandra data initiated."
        print(self.init_message)

    def __repr__(self):
        return f"Chandra object from path {self.path}"

    def get_objectname(self):
        """Returns the name of the object.
        """
        return self.objectname

    def get_filepath(self):
        """Returns the filepath of the current datafile.
        """
        return self.path

    def get_telescopes(self):
        """Returns the telescopes that have data for the object in question.
        """
        return self.telescopes

    def e_hist(self, min_e=0, max_e=float("inf"), e_list=None, nbins='auto', save=False):
        """ Makes a histogram over the specified range of energies. Optionally saves output as PNG in the current directory.
        """
        if e_list is not None:
            e_band = e_list
        else:
            evt_data = fits.getdata(self.path)
            energy = evt_data["energy"]
            min_thresh = evt_data["energy"] >= min_e
            max_thresh = evt_data["energy"] < max_e
            e_band = energy[min_thresh & max_thresh]
        plt.hist(e_band, bins=nbins)
        plt.title(
            f"{self.objectname} Energy Distribution | {min_e}—{max_e} eV")
        plt.xlabel("Energy (eV)")
        plt.ylabel("Count")
        if save == True:
            plt.savefig(
                f"{self.objectname}_ehist_{min_e}-{max_e}eV.png", dpi=250, format="png")
            print(f"Histogram saved to {os.getcwd()}.")
            plt.close()
        else:
            plt.show()

    def e_mask(self, min_e, max_e, inplace=False):
        """Returns list of masked energies, given a min and max value.
        """
        if inplace == False:
            evt_data = fits.getdata(self.path)
            energy = evt_data["energy"]
            min_thresh = evt_data["energy"] >= min_e
            max_thresh = evt_data["energy"] < max_e
            e_mask = energy[min_thresh & max_thresh]
            return e_mask
        else:
            pass


class XMM:
    """Takes a file path or name as input. As of now, this class can only initiate data, yield energy histograms, and apply energy masks.
    """

    def __init__(self, file):
        if os.path.isfile(file):
            self.path = file
        else:
            for path, _dir, files in os.walk(f"{data_dir}"):
                if file in files:
                    self.path = os.path.join(path, file)
        for item in objects.keys():
            if item in self.path:
                self.objectname = item
        obj_path = objects[self.objectname]
        self.telescopes = []
        for telescope in os.scandir(obj_path):
            if telescope.is_dir() and "." not in telescope.name:
                self.telescopes.append(telescope.name)
        if not "XMM" in self.telescopes:
            self.init_message = f"{self.objectname} has no data from the XMM-Newton telescope."
        else:
            self.init_message = "XMM-Newton data initiated."
        print(self.init_message)

    def __repr__(self):
        return f"XMM object from path {self.path}"

    def get_objectname(self):
        """Returns the name of the object.
        """
        return self.objectname

    def get_filepath(self):
        """Returns the filepath of the current datafile.
        """
        return self.path

    def get_telescopes(self):
        """Returns the telescopes that have data for the object in question.
        """
        return self.telescopes

    def e_hist(self, min_e=0, max_e=float("inf"), e_list=None, nbins='auto', save=False):
        """ Makes a histogram over the specified range of energies. Optionally saves output as PNG in the current directory.
        """
        if e_list is not None:
            e_band = e_list
        else:
            evt_data = fits.getdata(self.path)
            energy = evt_data["PI"]
            min_thresh = evt_data["PI"] >= min_e
            max_thresh = evt_data["PI"] < max_e
            e_band = energy[min_thresh & max_thresh]
        plt.hist(e_band, bins=nbins)
        plt.title(
            f"{self.objectname} Energy Distribution | {min_e}—{max_e} eV")
        plt.xlabel("Energy (eV)")
        plt.ylabel("Count")
        if save == True:
            plt.savefig(
                f"{self.objectname}_ehist_{min_e}-{max_e}eV.png", dpi=250, format="png")
            print(f"Histogram saved to {os.getcwd()}.")
            plt.close()
        else:
            plt.show()

    def e_mask(self, min_e=0, max_e=float("inf"), inplace=False):
        """
        """
        if inplace == False:
            evt_data = fits.getdata(self.path)
            energy = evt_data["PI"]
            min_thresh = evt_data["PI"] >= min_e
            max_thresh = evt_data["PI"] < max_e
            e_mask = energy[min_thresh & max_thresh]
            return e_mask
        else:
            pass


class Rosat:
    """
    """

    def __init__(self, file):
        pass

    def __repr__(self):
        # return f"Rosat object from path {self.path}"
        pass

    def e_hist(self, min_e=0, max_e=float("inf"), nbins='auto', save=False):
        pass


class Swift:
    """
    """

    def __init__(self, file):
        pass

    def __repr__(self):
        # return f"Swift object from path {self.path}"
        pass

    def e_hist(self, min_e=0, max_e=float("inf"), nbins='auto', save=False):
        pass
