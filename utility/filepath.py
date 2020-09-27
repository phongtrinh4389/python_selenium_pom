import os
import rootpath
from dotenv import load_dotenv


def get_root_directory():
    return rootpath.detect()


def get_full_path(*args):
    return os.path.join(get_root_directory(), *args)


def join_path(src, *args):
    return os.path.join(src, *args)


def get_secure_var(key):
    load_dotenv()
    return os.environ.get(key)


def file_exists(file_path):
    return os.path.isfile(file_path)


def dir_exists(directory):
    return os.path.isdir(directory)


def create_dir(directory):
    if not dir_exists(directory):
        os.makedirs(directory)
