import configparser
from pathlib import Path


def read_config() -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.read_file(open(Path(__file__).parent.parent / "config.ini"))
    return config
