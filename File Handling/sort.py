import os
import shutil

data_dir = "/Users/hunterholland/Documents/Research/Laidlaw/Data"

parent_dir_basename = "PPS"
new_folder_name = "img"
matched_phrases = ["IMAGE_"]


for directory, subdir, files in os.walk(f"{data_dir}"):
    if parent_dir_basename in os.path.basename(directory):
        if not new_folder_name in subdir:
            os.mkdir(f"{directory}/{new_folder_name}")
            for filename in files:
                for phrase in matched_phrases:
                    if phrase in filename:
                        shutil.move(f"{directory}/{filename}",
                                    f"{directory}/{new_folder_name}/{filename}")

folder_name = "14609920"
new_folder_name = "L1521E/Spitzer"

for directory, subdir, files in os.walk(f"{data_dir}"):
    if folder_name in os.path.basename(directory):
        old_name = directory
        new_name = f"{os.path.dirname(old_name)}/{new_folder_name}"
        os.rename(old_name, new_name)
        print("Done")
