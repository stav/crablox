from pathlib import Path

from fasthtml.common import A, Li, Ul, H3


def get_details(path: str, details_file: str) -> str:
    """
    Reads and returns the contents of the details markdown file.

    Args:
        path: The path to the caller file
        details_file: The name of the details markdown file to read

    Returns:
        str: The contents of the details markdown file
    """
    file = Path(path)
    details_path = Path(file.parent) / details_file
    return details_path.read_text()


def get_history(path: str):
    """
    Generates a list of historical files.

    Args:
        path: The path to the caller file

    Returns:
        Ul: An unordered list (HTML) containing links to historical files
    """
    file = Path(path)
    parent = file.parent
    files = [f.name for f in parent.glob("*.md")]
    return Ul(
        *[
            Li(
                A(
                    filename,
                    hx_get=f"/api/history/{parent.name}/{filename}",
                    hx_target="closest .wlv-data",
                )
            )
            for filename in sorted(files, reverse=True)
        ],
        cls="crb-history-list",
    )


def get_footer(resources: list[tuple[str, str]], history) -> tuple:
    """
    Generates a footer with resources and history sections.

    Args:
        resources: List of (name, url) tuples for resource links
        history: The history list component

    Returns:
        tuple: Footer components including resources and history sections
    """
    return (
        H3("Resources"),
        Ul(*[Li(A(name, href=url, target="_blank")) for name, url in resources]),
        H3("History"),
        history,
    )
