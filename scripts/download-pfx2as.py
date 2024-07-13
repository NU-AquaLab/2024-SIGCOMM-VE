"""
This script downloads routing data files from the CAIDA dataset by automatically generating URLs for required dates and then fetching the files.

The script uses CAIDA's Routeviews Prefix-to-AS mapping data to provide historical route views from 1998 to the current date. Files are downloaded monthly and stored locally.
"""

import os
import requests
from bs4 import BeautifulSoup
import wget
import rootpath
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Set the working directory to the root of the git repository
path = rootpath.detect(pattern=".git")
os.chdir(path)

# Define the start date for the data collection
STARTS = datetime(1998, 1, 1)

def get_resource_to_download(url):
    """
    Fetch the filename of the first available Routeviews Prefix-to-AS data file from the specified URL.

    Parameters
    ----------
    url : str
        The URL to fetch the available data files list.

    Returns
    -------
    str
        The filename of the first relevant data file, if found; otherwise, an empty string.
    """
    file_name = ''
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for href in soup.find_all('a'):
            if 'routeviews-rv2-' in href.text:
                file_name = href.text
                break

    return file_name

def main():
    """
    Main function to download Routeviews Prefix-to-AS mapping data files from CAIDA for each month starting from January 1998 to the current month.

    The function constructs URLs for each month, checks if the file already exists, and if not, downloads and stores it locally.
    """
    current_date = datetime.today()
    d = STARTS

    while d < current_date:
        date_str = d.strftime("%Y%m%d")
        filename = f"routeviews-rv2-{d.year}{d.month:02d}{d.day:02d}.pfx2as.gz"
        
        if not os.path.exists(filename):
            download_url = f"http://data.caida.org/datasets/routing/routeviews-prefix2as/{d.year}/{d.month:02d}/"
            pfix2as_file_name = get_resource_to_download(download_url)

            if pfix2as_file_name:
                try:
                    full_url = f"{download_url}{pfix2as_file_name}"
                    print(full_url)
                    wget.download(full_url, out=f"data/raw/02-pfx2as/{filename}")
                except Exception as e:
                    print(f"Failed to download {date_str}: {str(e)}")

        d += relativedelta(months=1)

if __name__ == "__main__":
    main()