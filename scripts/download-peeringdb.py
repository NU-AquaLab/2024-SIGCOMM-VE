"""
This script automates the download of monthly snapshots of PeeringDB data dumps from the CAIDA public dataset. 
It checks for the existence of files from April 2018 to December 2023, downloads them if they are not already stored locally, 
and then compresses and copies the files into another directory for archival purposes.
"""

import os
import wget

from datetime import datetime
from dateutil.relativedelta import relativedelta
from script_utils import configure_path, create_dir, log_info

configure_path()

# Define the start date for the data collection
START_DATE = datetime(2018, 4, 1)
END_DATE = datetime(2024, 1, 1)


def main():
    """
    Main function to manage the downloading process of PeeringDB data files.

    Iterates from a starting date to the current date,
    constructs the download URL and local storage path for each dataset,
    downloads it if it doesn't exist locally, compresses it, and copies it to another directory for archival.
    """
    d = START_DATE
    base_path = "data/raw/03-10-15-peeringdb"

    while d < END_DATE:
        date_str = d.strftime("%Y%m%d")
        snapshot = f"peeringdb_2_dump_{d.year}_{d.month:02d}_{d.day:02d}.json"
        filename = f"{base_path}/{snapshot}"

        if not os.path.exists(filename):
            create_dir(filename)

            try:
                log_info("PeeringDB", d)

                wget.download(
                    f"https://publicdata.caida.org/datasets/peeringdb-v2/{d.year}/{d.month:02d}/{snapshot}",
                    out=filename,
                )

                os.system(f"gzip -9 {filename}")
            except Exception as e:
                print(f"Failed to download {date_str}: {str(e)}")

        d += relativedelta(months=+1)


if __name__ == "__main__":
    main()
