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

# from transitlib.cfgLoader import cfgLoader

####################################################################

path = rootpath.detect(pattern=".git")
os.chdir(path)

# cfg = cfgLoader()

####################################################################

STARTS = datetime(2003, 1, 1)



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

        for rir in ["lacnic"]:


            url = "https://ftp.lacnic.net/pub/stats/lacnic/delegated-lacnic-{}".format(date_str)
            filename ="data/raw/delfiles/{}".format(url.split("/")[-1])


            if not os.path.exists(filename):
                _create_dir(filename)

                try:
                    wget.download(
                        url,
                        out=filename
                    )
                except:
                    print(f"{date_str} not found")


        d += relativedelta(months=+1)




if __name__ == "__main__":
    # execute only if run as a script
    main()