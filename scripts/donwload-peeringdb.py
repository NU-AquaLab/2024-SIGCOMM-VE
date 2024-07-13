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

STARTS = datetime(2018, 4, 1)

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
        
        if not os.path.exists(filename):
            
            path = "data/raw/03-15-peeringdb"
            filename = "peeringdb_2_dump_{d.year}_{d.month:02d}_{d.day:02d}.json"

            try:
                wget.download(
                    "https://publicdata.caida.org/datasets/peeringdb-v2/{d.year}/{d.month:02d}/{filename}",
                    out=filename
                )

                os.sytem("gzip -9 {path}/{filename}")
                os.sytem("cp data/raw/10-peeringdb/{filename}.gz")
            except:
                print(f"{date_str} not found")

        d += relativedelta(months=+1)




if __name__ == "__main__":
    # execute only if run as a script
    main()
