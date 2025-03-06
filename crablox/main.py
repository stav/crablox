from starlette.requests import Request
from fasthtml.common import fast_app, serve

import auth
import audio
import index
from config import env, fast_config

app, rt = fast_app(before=auth.beforeware, **fast_config)
print(f'Using "{env}" environment for {app}')
serve()


@rt("/")
def _(request: Request):
    return index.route(rt)


@rt("/audio/{id}")
def _(id: str):
    return audio.get_audio_file(id)


@app.get("/login")
def _(request: Request):
    return auth.login_page()


@app.post("/login")
async def _(request: Request):
    return await auth.login(request)


@rt("/logout")
def _(request: Request):
    return auth.logout(request)
