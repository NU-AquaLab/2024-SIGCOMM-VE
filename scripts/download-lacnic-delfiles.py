"""
This script automates the download of delegated internet number resource statistics from LACNIC. 
It checks for the existence of daily records from January 2003 to the present day and downloads them if they are not already stored locally. 
The data is saved under 'data/raw/08-delegated-lacnic/'.
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
STARTS = datetime(2003, 1, 1)

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
    Main function to manage the downloading process of delegated statistics from LACNIC.

    Iterates from a starting date to the current date, constructs the download URL and local storage path for each dataset, 
    then downloads it if it doesn't exist locally.
    """
    current_date = datetime.today()
    d = STARTS

    while d < current_date:
        date_str = d.strftime("%Y%m%d")
        url = f"https://ftp.lacnic.net/pub/stats/lacnic/delegated-lacnic-{date_str}"
        filename = f"data/raw/08-delegated-lacnic/delegated-lacnic-{date_str}"
        
        if not os.path.exists(filename):
            _create_dir(filename)
            try:
                wget.download(url, out=filename)
            except Exception as e:
                print(f"Failed to download {date_str}: {str(e)}")

        d += relativedelta(months=+1)

if __name__ == "__main__":
    main()