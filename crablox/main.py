from fasthtml.common import fast_app, serve

import auth
import routes
from config import env, fast_config, reload

app, rt = fast_app(before=auth.beforeware, **fast_config)
# app.htmlkw["data-theme"] = "dark"
print(f'Using "{env}" environment for {app}')

routes.register_routes(app, rt)

serve(reload=reload)
