import configparser
import os

from fh_altair import altair_headers
from style import styles


base_config = {
    "hdrs": [styles, altair_headers],
    "static_path": "./crablox",
}

dev_config = {
    "live": True,
    "debug": True,
    **base_config,
}

prod_config = {**base_config}

env = os.getenv("CRB", "production")

fast_config = prod_config if env == "production" else dev_config


# Read config file for certain keys
file_path = os.path.abspath(__file__)
parent_dir = os.path.dirname(file_path)
mixed_path = os.path.join(parent_dir, "..", "config.ini")
config_file_path = os.path.abspath(mixed_path)
config = configparser.ConfigParser()
config.read(config_file_path)

API_KEY = config["CMC"]["API_KEY"]
USERNAME = config["DEFAULT"]["USERNAME"]
