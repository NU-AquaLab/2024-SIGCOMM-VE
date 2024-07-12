"""
This script ???

To be filled
"""
import os.path
import os
from datetime import date, datetime, timedelta
from dateutil.relativedelta import *

import rootpath
import wget

####################################################################

path = rootpath.detect(pattern=".git")
os.chdir(path)


####################################################################

STARTS = datetime(1998, 1, 1)



def _create_dir(filename):

    dir_to_create = "/".join(filename.split("/")[:-1])

    if not os.path.exists('{}'.format(dir_to_create)):
        os.makedirs('{}'.format(dir_to_create))

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

        filename = "data/raw/asrel/{}.as-rel.txt.bz2".format(date_str)
        
        if not os.path.exists(filename):
            _create_dir(filename)

            try:
                wget.download(
                    "http://data.caida.org/datasets/as-relationships/serial-1/{}.as-rel.txt.bz2".format(date_str),
                    out=filename
                )
            except:
                print(f"{date_str} not found")

        d += relativedelta(months=+1)




if __name__ == "__main__":
    # execute only if run as a script
    main()
