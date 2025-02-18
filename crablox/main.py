from types import ModuleType

from starlette.responses import RedirectResponse
from starlette.requests import Request
from fasthtml.common import (
    Beforeware,
    A,
    Button,
    Div,
    fast_app,
    Form,
    Img,
    Input,
    Label,
    P,
    ScriptX,
    serve,
    Titled,
    Svg,
)
from fa6_icons import svgs

from config import env, fast_config, USERNAME

import hauls
from blocks import stack


def user_auth_before(req, sess):
    # The `auth` key in the request scope is automatically provided
    # to any handler which requests it, and can not be injected
    # by the user using query params, cookies, etc, so it should
    # be secure to use.
    auth = req.scope["auth"] = sess.get("auth", None)
    # If the session key is not there, it redirects to the login page.
    if not auth:
        # Status code 303 is a redirect that can change POST to GET,
        # so it's appropriate for a login page.
        return RedirectResponse("/login", status_code=303)


beforeware = Beforeware(
    user_auth_before,
    skip=[r"/favicon\.ico", r"/static/.*", r".*\.css", r".*\.js", "/login"],
)

app, rt = fast_app(before=beforeware, **fast_config)
print(f'Using "{env}" environment for {app}')


def create_route(block: ModuleType):
    """
    Creates a route for the given block.

    This function is a wrapper around the `rt` decorator to create a scope for
    the block object at runtime.

    This wrapper creates a route using the block's path. This route is a GET
    request handler that returns the contents of the block.

    Args:
        block: A module object representing a block with: path, id, title, content()

    Returns:
        None
    """

    @rt(block.path)
    def get():
        return block.content()


def block_stacker():
    """
    Generator function that processes hauls and yields a container for each
    block's: path, id, and title.

    Yields:
        The result of the stack function for each block.
    """
    for block in hauls.blocks:
        create_route(block)
        yield stack(block.path, block.id, block.title)


@rt
def index(req: Request):
    path = "crablox/main.js"
    return (
        Titled(
            "Indicator Megaboard Dashboard",
            Div(
                *block_stacker(),
                A(
                    Svg(
                        svgs.arrow_right_from_bracket.solid,
                    ),
                    href="/logout",
                    title="Logout",
                    style="width: 22em; display: flex;",
                ),
                cls="swapy-container",
            ),
            cls="flex flex-col lg:p-10 p-5 dark:bg-[hsl(220.91deg,39.29%,8%)] bg-[hsl(220.91deg,30.29%,94%)] rounded-lg",
        ),
        Div(
            Div(Img(id="lightbox-img"), cls="lightbox-image"),
            Div(id="lightbox-cap", cls="lightbox-caption"),
            Div(id="lightbox-det", cls="lightbox-details"),
            # X closes lightbox, also escape key listener in main.js
            Div(
                Button(
                    "X",
                    cls="crb-close",
                    data_swapy_no_drag=True,
                    title="Try me, or hit escape key",
                ),
                cls="lightbox-close",
                onclick="closeLightbox()",
            ),
            cls="lightbox",
            id="lightbox",
        ),
        ScriptX(path),
    )


@rt("/logout")
def logout(req: Request):
    req.session.clear()
    return RedirectResponse("/login", status_code=303)


@app.get("/login")
def login_page(req: Request):
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


@app.post("/login")
async def login(request: Request):
    form = await request.form()
    username = form.get("username")

    if username == USERNAME:
        request.session["auth"] = True

    return RedirectResponse("/", status_code=303)


serve()
