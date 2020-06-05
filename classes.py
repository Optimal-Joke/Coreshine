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


class Telescope:
    def __init__(self, file):
        if os.path.isfile(file):  # Assign input to filepath
            self.path = file
            self.file_dir, self.filename = os.path.split(file)
        else:  # Get filepath from file input
            for directory, _subdir, files in os.walk(f"{data_dir}"):
                if file in files:
                    self.path = os.path.join(directory, file)
                    self.file_dir = directory
                    self.filename = file
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


class Spitzer(Telescope):
    """
    """

    def __init__(self, file):
        self.telescope = "Spitzer"
        super().__init__(file)
        if not self.telescope in self.telescopes:
            init_message = f"{self.objectname} has no data from {self.telescope} telescope."
        else:
            init_message = f"{self.telescope} data initiated."
        print(init_message)

    def __repr__(self):
        return f"{self.telescope} object from path {self.path}"

    def e_hist(self, min_e, max_e, nbins='auto'):
        pass


class Chandra(Telescope):
    """Takes a file path or name as input. As of now, this class can initiate data, yield energy histograms, and filter files based on energy (photon intensity).
    """

    def __init__(self, file):
        self.telescope = "Chandra"
        super().__init__(file)
        if not self.telescope in self.telescopes:
            init_message = f"{self.objectname} has no data from {self.telescope} telescope."
        else:
            init_message = f"{self.telescope} data initiated."
        print(init_message)

    def __repr__(self):
        return f"{self.telescope} object from path {self.path}"

    def e_hist(self, min_e=0, max_e=float("inf"), e_list=None, e_list2=None, nbins='auto', object=False, save=False, filename=None):
        """Makes a histogram over the specified range of energies or of up to two lists of energies passed as input. Optionally saves output as PNG active file's directory.
        """
        if e_list is not None:
            e_band = e_list
        else:
            evt_data = fits.getdata(self.path)
            energy = evt_data["energy"]
            min_thresh = energy >= min_e
            max_thresh = energy < max_e
            e_band = energy[min_thresh & max_thresh]
        plt.hist(e_band, bins=nbins)
        if e_list2 is not None:
            plt.hist(e_list2, bins=nbins)
        plt.xlabel("Energy (eV)")
        plt.ylabel("Count")
        if not object:
            plt.title(
                f"Energy Distribution")
        elif object:
            plt.title(
                f"{object} Energy Distribution")
        if save == True:
            if object:
                if filename is None:
                    plt.savefig(
                        f"{self.file_dir}/ehist.png", dpi=250, format="png")
                else:
                    plt.savefig(
                        f"{self.file_dir}/{filename}", dpi=250, format="png")
                print(f"Histogram saved to {self.file_dir}.")
            else:
                if filename is None:
                    print(
                        f"Histogram is not of a specified object, so you must specify a filename.\nNo file saved.")
                    return
                else:
                    plt.savefig(
                        f"{self.file_dir}/{filename}", dpi=250, format="png")
                    print(f"Histogram saved to {self.file_dir}.")
            plt.close()
        else:
            plt.show()

    def e_mask(self, range1=list, *args, newfile=False, filename=None):
        """If newfile=False, method returns a list of masked energies that fall within the given ranges. Each range should be specifed as a list of length 2. For example, a range of energies from 600-1000eV would be denoted [600, 1000]. The final range may be of length 1 — for example, [1000]. This defaults to a range [1000, infinity].

        If newfile=True, a new file will be created that only contains rows with energies within the specified ranges.
        """
        evt_data = fits.getdata(self.path)  # Get event data from file
        energy = evt_data["energy"]  # Get energy data from event data
        try:  # If a range with a max and min is passed as input.
            min_e, max_e = range1
        except ValueError:  # If a range with only a min is passed as input.
            min_e, max_e = range1, float("inf")
        except TypeError:  # If no range is passed as input.
            min_e, max_e = 0, float("inf")
        # Create boolean filter list based on the energy data. This will be referenced and altered by each successive range passed as input.
        filter_list = (energy >= min_e) & (energy < max_e)
        for arg in args:
            try:  # If a range with a max and min is passed as input.
                min_e, max_e = arg
            except ValueError:  # If a range with only a min is passed as input.
                min_e, max_e = arg, float("inf")
            # New filter list with next provided range.
            r = (energy >= min_e) & (energy < max_e)
            # Iterate through each value of the master filter list. If the corresponding index in the new filter list is True, the value at that same index in master list will change to True.
            for i in range(len(filter_list)):
                if r[i] == True:
                    filter_list[i] = True
            # Master filter list (filter_list) is now an ordered list of bools. For each value in the energy data, if it is within the specified energy ranges, the corresponding index in filter_list is now True.
        if newfile == False:
            energies = energy[filter_list]
            return energies  # Return list of filtered energies.
        else:
            with fits.open(self.path) as hdul:
                evt_table = hdul[1]
                evt_table.data = evt_table.data[filter_list]
                if filename is None:
                    filename = f"{self.filename}"
                try:
                    hdul.writeto(filename)
                    print(f"Data filtered into file {filename}")
                except NameError:
                    print(
                        f"""A file with the name {filename} already exists in {os.getcwd()}\nPlease use the \"filename\" parameter to give it another name""")
                except OSError:
                    print(
                        f"""A file with the name {filename} already exists in {os.getcwd()}\nPlease use the \"filename\" parameter to give it another name""")


class XMM(Telescope):
    """Takes a file path or name as input. As of now, this class can initiate data, yield energy histograms, and filter files based on energy (photon intensity).
    """

    def __init__(self, file):
        self.telescope = "XMM"
        super().__init__(file)
        if not self.telescope in self.telescopes:
            init_message = f"{self.objectname} has no data from {self.telescope} telescope."
        else:
            init_message = f"{self.telescope} data initiated."
        print(init_message)

    def __repr__(self):
        return f"{self.telescope} object from path {self.path}"

    def e_hist(self, min_e=0, max_e=float("inf"), e_list=None, e_list2=None, nbins='auto', object=False, save=False, filename=None):
        """Makes a histogram over the specified range of energies or of up to two lists of energies passed as input. Optionally saves output as PNG active file's directory.
        """
        if e_list is not None:
            e_band = e_list
        else:
            evt_data = fits.getdata(self.path)
            energy = evt_data["energy"]
            min_thresh = energy >= min_e
            max_thresh = energy < max_e
            e_band = energy[min_thresh & max_thresh]
        plt.hist(e_band, bins=nbins)
        if e_list2 is not None:
            plt.hist(e_list2, bins=nbins)
        plt.xlabel("Energy (eV)")
        plt.ylabel("Count")
        if not object:
            plt.title(
                f"Energy Distribution")
        elif object:
            plt.title(
                f"{object} Energy Distribution")
        if save == True:
            if object:
                if filename is None:
                    plt.savefig(
                        f"{self.file_dir}/ehist.png", dpi=250, format="png")
                else:
                    plt.savefig(
                        f"{self.file_dir}/{filename}", dpi=250, format="png")
                print(f"Histogram saved to {self.file_dir}.")
            else:
                if filename is None:
                    print(
                        f"Histogram is not of a specified object, so you must specify a filename.\nNo file saved.")
                    return
                else:
                    plt.savefig(
                        f"{self.file_dir}/{filename}", dpi=250, format="png")
                    print(f"Histogram saved to {self.file_dir}.")
            plt.close()
        else:
            plt.show()

    def e_mask(self, range1=list, *args, newfile=False, filename=None):
        """If newfile=False, method returns a list of masked energies that fall within the given ranges. Each range should be specifed as a list of length 2. For example, a range of energies from 600-1000eV would be denoted [600, 1000]. The final range may be of length 1 — for example, [1000]. This defaults to a range [1000, infinity].

        If newfile=True, a new file will be created that only contains rows with energies within the specified ranges.
        """
        evt_data = fits.getdata(self.path)  # Get event data from file
        energy = evt_data["PI"]  # Get energy data from event data
        try:  # If a range with a max and min is passed as input.
            min_e, max_e = range1
        except ValueError:  # If a range with only a min is passed as input.
            min_e, max_e = range1, float("inf")
        except TypeError:  # If no range is passed as input.
            min_e, max_e = 0, float("inf")
        # Create boolean filter list based on the energy data. This will be referenced and altered by each successive range passed as input.
        filter_list = (energy >= min_e) & (energy < max_e)
        for arg in args:
            try:  # If a range with a max and min is passed as input.
                min_e, max_e = arg
            except ValueError:  # If a range with only a min is passed as input.
                min_e, max_e = arg, float("inf")
            # New filter list with next provided range.
            r = (energy >= min_e) & (energy < max_e)
            # Iterate through each value of the master filter list. If the corresponding index in the new filter list is True, the value at that same index in master list will change to True.
            for i in range(len(filter_list)):
                if r[i] == True:
                    filter_list[i] = True
            # Master filter list (filter_list) is now an ordered list of bools. For each value in the energy data, if it is within the specified energy ranges, the corresponding index in filter_list is now True.
        if newfile == False:
            energies = energy[filter_list]
            return energies  # Return list of filtered energies.
        else:
            with fits.open(self.path) as hdul:
                evt_table = hdul[1]
                evt_table.data = evt_table.data[filter_list]
                if filename is None:
                    filename = f"{self.filename}"
                try:
                    hdul.writeto(filename)
                    print(f"Data filtered into file {filename}")
                except NameError:
                    print(
                        f"""A file with the name {filename} already exists in {os.getcwd()}\nPlease use the \"filename\" parameter to give it another name""")
                except OSError:
                    print(
                        f"""A file with the name {filename} already exists in {os.getcwd()}\nPlease use the \"filename\" parameter to give it another name""")


class Rosat(Telescope):
    """
    """

    def __init__(self, file):
        self.telescope = "Rosat"
        super().__init__(file)
        if not self.telescope in self.telescopes:
            init_message = f"{self.objectname} has no data from {self.telescope} telescope."
        else:
            init_message = f"{self.telescope} data initiated."
        print(init_message)

    def __repr__(self):
        return f"{self.telescope} object from path {self.path}"

    def e_hist(self, min_e=0, max_e=float("inf"), nbins='auto', save=False):
        pass


class Swift(Telescope):
    """
    """

    def __init__(self, file):
        self.telescope = "Swift"
        super().__init__(file)
        if not self.telescope in self.telescopes:
            init_message = f"{self.objectname} has no data from {self.telescope} telescope."
        else:
            init_message = f"{self.telescope} data initiated."
        print(init_message)

    def __repr__(self):
        return f"{self.telescope} object from path {self.path}"

    def e_hist(self, min_e=0, max_e=float("inf"), nbins='auto', save=False):
        pass
