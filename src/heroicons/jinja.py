from markupsafe import Markup

import heroicons


def heroicon_outline(name: str, *, size: int = 24, **kwargs: object) -> str:
    return _render_icon("outline", name, size, **kwargs)


def heroicon_solid(name: str, *, size: int = 20, **kwargs: object) -> str:
    return _render_icon("solid", name, size, **kwargs)


def _render_icon(style: str, name: str, size: int, **kwargs: object) -> str:
    return Markup(heroicons._render_icon(style, name, size, **kwargs))
