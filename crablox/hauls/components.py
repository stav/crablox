from pathlib import Path

from fasthtml.common import A, Li, Ul, H3


def get_details(file_name: str) -> str:
    """
    Reads and returns the contents of the details markdown file.

    Args:
        file_name: The path to the caller file

    Returns:
        str: The contents of the details markdown file
    """
    file = Path(file_name)
    details_path = Path(file.parent) / f"{file.stem}|.md"
    return details_path.read_text()


def get_history(file_name: str):
    """
    Generates a list of historical files.

    Args:
        file_name: The path to the caller file

    Returns:
        Ul: An unordered list (HTML) containing links to historical files
    """
    file = Path(file_name)
    files = [f.name for f in file.parent.glob(f"{file.stem}*") if f.name != file.name]
    return Ul(
        *[
            Li(
                A(
                    filename,
                    hx_get=f"/api/history/{filename}",
                    hx_target="closest .wlv-data",
                )
            )
            for filename in sorted(files)
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
