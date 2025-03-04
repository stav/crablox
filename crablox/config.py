import configparser
import os

from fasthtml.common import Link, MarkdownJS, Script, StyleX
from fh_altair import altair_headers


base_config = {
    "hdrs": [
        Link(rel="icon", href="/static/favicon.ico"),
        altair_headers,
        StyleX("crablox/main.css"),
        MarkdownJS(),
        Script(src="https://unpkg.com/swapy/dist/swapy.min.js"),
    ],
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

SPEECHIFY_API_KEY = config["SPEECHIFY"]["API_KEY"]
CMC_API_KEY = config["CMC"]["API_KEY"]
AUTH_USERNAME = config["DEFAULT"]["AUTH_USERNAME"]
