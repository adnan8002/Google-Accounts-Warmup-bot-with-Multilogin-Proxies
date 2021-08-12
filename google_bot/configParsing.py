# depreciated
import configparser
import os


def get_filename(filename, section="FILES"):
    config = configparser.ConfigParser()
    config.read('filePaths.ini')
    return config.get(section, filename)


def get_dir():
    return os.path.dirname(os.path.abspath(__file__))


if __name__ == "__main__":
    print(get_dir())
