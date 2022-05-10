import configparser
import os
from pathlib import Path


def read_config() -> configparser.ConfigParser:
    """
    Reads test config into a dictionary
    """
    config = configparser.ConfigParser()
    config.read_file(open(Path(__file__).parent.parent / "config.ini"))
    return config


def run_headless() -> bool:
    """
    Whether tests are to be run in headless mode (set to True for Docker)
    """
    return os.getenv("RUN_HEADLESS", False)
