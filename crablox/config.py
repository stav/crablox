import configparser
import os

from fasthtml.common import Link, MarkdownJS, ScriptX, StyleX
from fh_altair import altair_headers


base_config = {
    "hdrs": [
        Link(rel="icon", href="/static/favicon.ico"),
        Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.colors.css"),
        altair_headers,
        StyleX("crablox/main.css"),
        MarkdownJS(),
        ScriptX("vendor/swapy/swapy.min.js"),
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

reload = env != "production"

fast_config = prod_config if env == "production" else dev_config


# Read config file for certain keys
file_path = os.path.abspath(__file__)
parent_dir = os.path.dirname(file_path)
mixed_path = os.path.join(parent_dir, "..", "config.ini")
config_file_path = os.path.abspath(mixed_path)
config = configparser.ConfigParser()
config.read(config_file_path)

CMC_API_KEY = config["CMC"]["API_KEY"]
AUTH_USERNAME = config["DEFAULT"]["AUTH_USERNAME"]
