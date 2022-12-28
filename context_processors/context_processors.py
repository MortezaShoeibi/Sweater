from home.models import Footer


def footer(request) -> object:
    footer = Footer.objects.last()
    return {'footer': footer}
