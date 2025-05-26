from starlette.requests import Request
from fasthtml.common import Div
from pathlib import Path

import auth
import audio
import blocks
import hauls
import index
import ticker

def register_routes(app, rt):
    @rt("/")
    def _():
        return index.route(rt)

    @rt("/api/blocks/{id}")
    def _(id: str):
        for block in hauls.blocks:
            if block.id == id:
                return blocks.stack(block)
        return f"Block not found: {id}", 404

    @rt("/api/history/{parent}/{filename}")
    def _(parent: str, filename: str):
        file_path = Path("crablox/hauls") / parent / filename
        markup = file_path.read_text()
        return Div(markup, cls="marked")

    @rt("/api/lookup")
    def _(request: Request):
        return ticker.display(request)

    @rt("/api/search")
    def _(request: Request):
        return ticker.search(request)

    @rt("/audio/{id}")
    def _(id: str):
        return audio.get_audio_file(id)

    @app.get("/login")
    def _(request: Request):
        return auth.login_page(request)

    @app.post("/login")
    async def _(request: Request):
        return await auth.login(request)

    @rt("/logout")
    def _(request: Request):
        return auth.logout(request)

    @rt("/timeseries")
    def _(request: Request):
        ticker_param = request.query_params.get("ticker", "X")
        return ticker.time_series_table(ticker=ticker_param.upper()) 
