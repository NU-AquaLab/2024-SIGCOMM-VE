"""
This script automates the download of delegated internet number resource statistics from LACNIC. 
It checks for the existence of daily records from January 2003 to the present day and downloads them if they are not already stored locally. 
The data is saved under 'data/raw/08-delegated-lacnic/'.
"""

import os
import wget

from datetime import datetime
from dateutil.relativedelta import relativedelta
from script_utils import configure_path, create_dir, log_info

configure_path()

# Define the start date for the data collection
START_DATE = datetime(2004, 1, 1)


def main():
    """
    Main function to manage the downloading process of delegated statistics from LACNIC.

    Iterates from a starting date to the current date, constructs the download URL and local storage path for each dataset,
    then downloads it if it doesn't exist locally.
    """
    current_date = datetime.today()
    d = START_DATE

    while d < current_date:
        date_str = d.strftime("%Y%m%d")
        url = f"https://ftp.lacnic.net/pub/stats/lacnic/delegated-lacnic-{date_str}"
        filename = f"data/raw/08-delegated-lacnic/delegated-lacnic-{date_str}"

        if not os.path.exists(filename):
            create_dir(filename)

            try:
                log_info("LACNIC delegations", d)
                wget.download(url, out=filename)
            except Exception as e:
                print(f"Failed to download {date_str}: {str(e)}")

        d += relativedelta(months=+1)


if __name__ == "__main__":
    main()
