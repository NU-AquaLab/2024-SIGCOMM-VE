import matplotlib
import os
import rootpath


def setup_matplotlib():
    matplotlib.rcParams["pdf.fonttype"] = 42
    matplotlib.rcParams["ps.fonttype"] = 42


def configure_path():
    path = rootpath.detect(pattern=".git")
    os.chdir(path)
