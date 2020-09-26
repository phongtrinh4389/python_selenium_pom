import sys
import os
import tarfile
import rootpath
from dotenv import load_dotenv
import json


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


def dir_exists(dir):
    return os.path.isdir(dir)


def create_dir(dir):
    if not dir_exists(dir):
        os.makedirs(dir)