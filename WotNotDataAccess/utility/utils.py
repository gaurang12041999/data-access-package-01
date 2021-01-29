import os

from io import StringIO
from configparser import ConfigParser


def read_properties_file(file_path):
    with open(file_path) as f:
        config = StringIO()
        config.write('[dummy_section]\n')
        config.write(f.read().replace('%', '%%'))
        config.seek(0, os.SEEK_SET)
        cp = ConfigParser()
        cp.read_file(config)
        return dict(cp.items('dummy_section'))
