from starlette.requests import Request
from fasthtml.common import Div
from pathlib import Path

import auth
import audio
import blocks
import hauls
import index
import ticker

def register(app):
    @app.route("/")
    def _():
        return index.route(app.route)

    @app.route("/api/blocks/{id}")
    def _(id: str):
        for block in hauls.blocks:
            if block.id == id:
                return blocks.stack(block)
        return f"Block not found: {id}", 404

    @app.route("/api/history/{parent}/{filename}")
    def _(parent: str, filename: str):
        file_path = Path("crablox/hauls") / parent / filename
        markup = file_path.read_text()
        return Div(markup, cls="marked")

    @app.route("/api/lookup")
    def _(request: Request):
        return ticker.display(request)

    @app.route("/api/search")
    def _(request: Request):
        return ticker.search(request)

    @app.route("/audio/{id}")
    def _(id: str):
        return audio.get_audio_file(id)

    @app.get("/login")
    def _(request: Request):
        return auth.login_page(request)

    @app.post("/login")
    async def _(request: Request):
        return await auth.login(request)

    @app.route("/logout")
    def _(request: Request):
        return auth.logout(request)

    @app.route("/timeseries")
    def _(request: Request):
        ticker_param = request.query_params.get("ticker", "")
        return ticker.time_series_table(ticker=ticker_param.upper())

    @app.route("/timeseries1")
    def _(request: Request):
        ticker_param = request.query_params.get("ticker", "")
        return ticker.time_series_table_excel(ticker=ticker_param.upper())

    @app.route("/timeseries2")
    def _(request: Request):
        ticker_param = request.query_params.get("ticker", "")
        return ticker.time_series_table_yahoo(ticker=ticker_param.upper()) 
