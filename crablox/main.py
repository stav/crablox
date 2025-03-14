from starlette.requests import Request
from fasthtml.common import fast_app, serve

import auth
import audio
import index
from config import env, fast_config

app, rt = fast_app(before=auth.beforeware, **fast_config)
print(f'Using "{env}" environment for {app}')
serve()

# Routes
#######################################################
# /                 | index  | Home page
# /login            | auth   | Login page & service
# /logout           | auth   | Logout service
# /audio/{id}       | audio  | Get audio file by id
# /static/{file}    |        | Get static files by name
# /api/blocks/{id}  | index  | Get block by id
# /favicon.ico      | config | /static/favicon.ico


@rt("/")
def _():
    return index.route(rt)


@rt("/audio/{id}")
def _(id: str):
    return audio.get_audio_file(id)


@app.get("/login")
def _():
    return auth.login_page()


@app.post("/login")
async def _(request: Request):
    return await auth.login(request)


@rt("/logout")
def _(request: Request):
    return auth.logout(request)
