"""
This script automates the download of monthly snapshots of PeeringDB data dumps from the CAIDA public dataset. 
It checks for the existence of files from April 2018 to the current date, downloads them if they are not already stored locally, 
and then compresses and copies the files into another directory for archival purposes.
"""

import os
import wget
from datetime import datetime
from dateutil.relativedelta import relativedelta
import rootpath

# Set the working directory to the root of the git repository
path = rootpath.detect(pattern=".git")
os.chdir(path)

# Define the start date for the data collection
STARTS = datetime(2018, 4, 1)

def _create_dir(filename):
    """
    Create a directory for the given filename if it doesn't already exist.

    Parameters
    ----------
    filename : str
        The path to the file for which the directory needs to be created.
    """
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)

def main():
    """
    Main function to manage the downloading process of PeeringDB data files.

    Iterates from a starting date to the current date, 
    constructs the download URL and local storage path for each dataset, 
    downloads it if it doesn't exist locally, compresses it, and copies it to another directory for archival.
    """
    current_date = datetime.today()
    d = STARTS
    base_path = "data/raw/03-15-peeringdb"

    while d < current_date:
        date_str = d.strftime("%Y%m%d")
        snapshot = f"peeringdb_2_dump_{d.year}_{d.month:02d}_{d.day:02d}.json"
        filename = f"{base_path}/{snapshot}"
        
        if not os.path.exists(filename):
            _create_dir(filename)
            try:
                wget.download(
                    f"https://publicdata.caida.org/datasets/peeringdb-v2/{d.year}/{d.month:02d}/{snapshot}",
                    out=filename
                )
                os.system(f"gzip -9 {filename}")
                os.system(f"cp {filename}.gz data/raw/10-peeringdb/")
            except Exception as e:
                print(f"Failed to download {date_str}: {str(e)}")

        d += relativedelta(months=+1)

if __name__ == "__main__":
    main()