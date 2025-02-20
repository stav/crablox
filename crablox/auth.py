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
    serve,
    Titled,
)

from config import USERNAME


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
    skip=[r"/favicon\.ico", r"/static/.*", r".*\.css", r".*\.js", "/login"],
)


def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/login", status_code=303)


def login_page():
    return Titled(
        "Indicator Megaboard Dashboard Login",
        P(
            A(
                "Get the username from the group.",
                href="https://www.skool.com/tradingbusiness/graphical-indicator-dashboard",
                target="_blank",
            )
        ),
        Form(
            Label("Username:", For="username"),
            Div(
                Input(
                    id="username",
                    name="username",
                    type="text",
                    required=True,
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
    username = form.get("username")

    if username == USERNAME:
        request.session["auth"] = True

    return RedirectResponse("/", status_code=303)


serve()
