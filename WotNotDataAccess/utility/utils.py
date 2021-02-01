import os


class Messenger:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs


def make_dir(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
