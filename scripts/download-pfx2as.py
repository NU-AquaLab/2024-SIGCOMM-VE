"""
This script ???

To be filled
"""

import os
import glob
from datetime import date, datetime, timedelta
from dateutil.relativedelta import *

import requests
from bs4 import BeautifulSoup
import rootpath
import wget

####################################################################

path = rootpath.detect(pattern=".git")
os.chdir(path)

####################################################################

STARTS = datetime(1998, 1, 1)
# STARTS = datetime(2023, 1, 1)

def get_resource_to_download(url):
    """
    Thi is an example script.

    It seems that it has to have THIS docstring with a summary line, a blank line
    and sume more text like here. Wow.
    """
    file_name = ''
    # Gets pfix2as archive website
    response = requests.get(url)

    if response.status_code == 200:
        # Data transformation
        soup = BeautifulSoup(response.text)
        # Look for href to files
        pfix2as_website_href_list = soup.find_all('a')
        for href in pfix2as_website_href_list:
            # First file that contains 'routeviews-rv2-' is the first monthly snapshot
            if 'routeviews-rv2-' in href.text:
                file_name = href.text
                break

    return file_name


def main():
    """
    Thi is an example script.

    It seems that it has to have THIS docstring with a summary line, a blank line
    and sume more text like here. Wow.
    """
    # creates output dir


    d = STARTS
    ends = datetime.today()

    while d < ends:

        date_str = d.strftime("%Y%m%d")

        filename = f"routeviews-rv2-{d.year}{d.month:02d}{d.day:02d}.pfx2as.gz"
        
        if not os.path.exists(filename):

            pfix2as_file_name = get_resource_to_download(
                f'http://data.caida.org/datasets/routing/routeviews-prefix2as/{d.year}/{d.month:02d}/'
            )

            if pfix2as_file_name != '':


                # wget.download(
                #     f"http://data.caida.org/datasets/routing/routeviews-prefix2as/{d.year}/{d.month:02d}/{pfix2as_file_name}",
                #     out=f"data/raw/pfx2as/{filename}"
                # )

                try:
                    # https://data.caida.org/datasets/routing/routeviews-prefix2as/2008/12/routeviews-rv2-20081229-1302.pfx2as.gz
                    print(f"http://data.caida.org/datasets/routing/routeviews-prefix2as/{d.year}/{d.month:02d}/{pfix2as_file_name}",)
                    wget.download(
                        f"http://data.caida.org/datasets/routing/routeviews-prefix2as/{d.year}/{d.month:02d}/{pfix2as_file_name}",
                        out=f"data/raw/pfx2as/{filename}"
                    )
                except:
                    print(f"{date_str} not found")

        d += relativedelta(months=+1)



if __name__ == "__main__":
    # execute only if run as a script
    main()
