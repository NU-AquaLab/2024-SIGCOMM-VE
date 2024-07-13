import os
import rootpath


def configure_path():
    """
    Configure the working directory to the root of the git repository.
    """
    path = rootpath.detect(pattern=".git")
    os.chdir(path)


def create_dir(filename):
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


def log_info(type, date):
    print()
    print(f"Downloading {type} data for {date.strftime('%Y-%m')}")
