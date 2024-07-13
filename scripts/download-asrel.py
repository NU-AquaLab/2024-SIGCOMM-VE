"""
This script automates the download of AS-relationship datasets from the CAIDA website. 
It checks for the existence of files for each month from January 1998 to December 2023 and downloads them if they are not already stored locally. 
The datasets are saved in a structured directory format under 'data/raw/08-asrel/'.
"""

import os
import wget

from datetime import datetime
from dateutil.relativedelta import relativedelta
from script_utils import configure_path, create_dir, log_info

configure_path()

# Define the start date for the data collection
START_DATE = datetime(1998, 1, 1)
END_DATE = datetime(2024, 1, 1)


def main():
    """
    Main function to manage the downloading process of AS-relationship datasets.

    The function iterates from a starting date to the current date, constructing the download URL and local storage path for each dataset, and then downloads it if it doesn't exist locally.
    """
    d = START_DATE

    while d < END_DATE:
        date_str = d.strftime("%Y%m%d")
        filename = f"data/raw/08-asrel/{date_str}.as-rel.txt.bz2"

        if not os.path.exists(filename):
            create_dir(filename)

            download_url = f"http://data.caida.org/datasets/as-relationships/serial-1/{date_str}.as-rel.txt.bz2"

            try:
                log_info("as-relatioships", d)
                wget.download(download_url, out=filename)
            except Exception as e:
                print(f"Failed to download {date_str}: {str(e)}")

        d += relativedelta(months=+1)


if __name__ == "__main__":
    main()
