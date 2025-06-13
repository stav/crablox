import logging

from fasthtml.common import fast_app, serve

import auth
import routes

from config import env, fast_config, reload
from log import configure_logging

configure_logging()

app, _ = fast_app(before=auth.beforeware, **fast_config)
# app.htmlkw["data-theme"] = "dark"
logger = logging.getLogger(__name__)
logger.info(f'Using "{env}" environment for {app}')

routes.register(app)

serve(reload=reload)
