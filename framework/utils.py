import configparser
import os
from pathlib import Path


def read_config() -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.read_file(open(Path(__file__).parent.parent / "config.ini"))
    return config


def run_headless() -> bool:
    return os.getenv("RUN_HEADLESS", False)
