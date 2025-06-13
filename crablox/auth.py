from starlette.responses import RedirectResponse
from starlette.requests import Request
from fasthtml.common import (
    Beforeware,
    A,
    Button,
    Div,
    Form,
    Input,
    Label,
    P,
    Titled,
)
import logging

from config import AUTH_USERNAME

logger = logging.getLogger(__name__)


def user_auth_before(request, sess):
    # The `auth` key in the request scope is automatically provided
    # to any handler which requests it, and can not be injected
    # by the user using query params, cookies, etc, so it should
    # be secure to use.
    auth = request.scope["auth"] = sess.get("auth", None)
    # If the session key is not there, it redirects to the login page.
    if not auth:
        # Status code 303 is a redirect that can change POST to GET,
        # so it's appropriate for a login page.
        return RedirectResponse("/login", status_code=303)


beforeware = Beforeware(
    user_auth_before,
    skip=[
        r"/favicon\.ico",
        r"/static/.*",
        r".*\.css",
        r".*\.js",
        "/login",
        r"/live-reload",  # Skip live reload WebSocket
    ],
)


def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/login", status_code=303)


def login_page(request: Request | None = None):
    # If we have a request and are already logged in, redirect to home
    if request and request.session.get("auth"):
        logger.info("Login page - We're already logged in, redirecting to app")
        return RedirectResponse("/", status_code=303)
    
    # Get any error message from the session
    error_msg = request.session.pop("login_error", None) if request else None
        
    return Titled(
        "Megaboard Indicator Blocks Login",
        P(
            A(
                "Get the username from the group.",
                href="https://www.skool.com/tradingbusiness/graphical-indicator-dashboard",
                target="_blank",
            )
        ),
        *([Div(error_msg, style="color: red; margin-bottom: 1em;")] if error_msg else []),
        Form(
            Label("Username:", For="username"),
            Div(
                Input(
                    id="username",
                    name="username",
                    type="text",
                    required=True,
                    autofocus=True,
                ),
            ),
            Div(Button("Login", type="submit")),
            action="/login",
            method="post",
        ),
        style="max-width: 400px; margin: auto;",
    )


async def login(request: Request):
    form = await request.form()
    client_username = str(form.get("username"))

    if client_username.lower() == AUTH_USERNAME.lower():
        request.session["auth"] = True
        logger.info(f"Login successful - Session after set: {request.session}")
        # Use a more direct redirect with additional headers to prevent caching and extra requests
        response = RedirectResponse(url="/", status_code=303)
        response.headers.update({
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0",
            "X-Accel-Buffering": "no",  # Prevent buffering
            "Connection": "close",  # Close connection after response
        })
    else:
        logger.info(f"Login failed - Session after set: {request.session}")
        request.session["login_error"] = "Invalid username"
        response = RedirectResponse(url="/login", status_code=303)
        response.headers.update({
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0",
        })

    return response
    