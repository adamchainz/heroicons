from markupsafe import Markup

import heroicons


def heroicon_outline(name, *, size=24, **kwargs):
    return _heroicon("outline", name, size, **kwargs)


def heroicon_solid(name, *, size=20, **kwargs):
    return _heroicon("solid", name, size, **kwargs)


def _heroicon(style, name, size, **kwargs):
    svg = heroicons.load_icon(style, name)
    start = '<svg width="{}" height="{}" '
    if kwargs:
        start += " ".join(f'{name.replace("_", "-")}="{{}}"' for name in kwargs)
        start += " "

    svg = Markup(svg.replace("<svg ", start, 1))
    return svg.format(size, size, *kwargs.values())
