# Change the range as needed for your dataset

import os

script_dir = os.path.dirname(os.path.realpath(__file__))

for year in range(1999, 2004):
    os.makedirs(os.path.join(script_dir, str(year)), exist_ok=True)
