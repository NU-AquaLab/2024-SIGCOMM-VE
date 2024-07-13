"""
This script downloads routing data files from the CAIDA dataset by automatically generating URLs for required dates and then fetching the files.

The script uses CAIDA's Routeviews Prefix-to-AS mapping data to provide historical route views from June 2008 to December 2023. Files are downloaded monthly and stored locally.
"""

import os
import requests
import wget

from bs4 import BeautifulSoup
from datetime import datetime
from dateutil.relativedelta import relativedelta
from script_utils import configure_path, log_info

configure_path()

# Define the start date for the data collection
START_DATE = datetime(2009, 6, 1)
END_DATE = datetime(2024, 1, 1)


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
    file_name = ""
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        for href in soup.find_all("a"):
            if "routeviews-rv2-" in href.text:
                file_name = href.text
                break

    return file_name


def main():
    """
    Main function to download Routeviews Prefix-to-AS mapping data files from CAIDA for each month starting from January 1998 to the current month.

    The function constructs URLs for each month, checks if the file already exists, and if not, downloads and stores it locally.
    """
    d = START_DATE

    while d < END_DATE:
        date_str = d.strftime("%Y%m%d")
        filename = f"routeviews-rv2-{d.year}{d.month:02d}{d.day:02d}.pfx2as.gz"

        if not os.path.exists(filename):
            download_url = f"http://data.caida.org/datasets/routing/routeviews-prefix2as/{d.year}/{d.month:02d}/"
            pfix2as_file_name = get_resource_to_download(download_url)
            full_url = f"{download_url}{pfix2as_file_name}"

            if pfix2as_file_name:
                try:
                    log_info("prefix2as", d)
                    wget.download(full_url, out=f"data/raw/02-pfx2as/{filename}")
                except Exception as e:
                    print(f"Failed to download {date_str}: {str(e)}")

        d += relativedelta(months=1)


if __name__ == "__main__":
    main()
