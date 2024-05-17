#Change the range as needed for your dataset

import os

script_dir = os.path.dirname(os.path.realpath(__file__))

for year in range(1999, 2004):
    month = 1
    year_folder = os.path.join(script_dir, str(year))
    files_in_year = sorted(os.listdir(year_folder))
    for filename in files_in_year:
        if os.path.isfile(os.path.join(year_folder, filename)):
            new_filename = f"{month:02d}_{year % 100:02d}.tif"
            os.rename(os.path.join(year_folder, filename), os.path.join(year_folder, new_filename))
            month += 1
