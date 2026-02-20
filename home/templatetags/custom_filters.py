from django import template

register = template.Library()


@register.filter(name='split')
def split(value, sep=','):
    """Split a string by `sep` and return a list. Returns empty list for None."""
    if value is None:
        return []
    try:
        return [part.strip() for part in value.split(sep) if part.strip()]
    except Exception:
        return []
