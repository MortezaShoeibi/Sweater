from core.models import Footer


def footer(request) -> dict:
    footer = Footer.objects.last()
    if footer != None:
        pre_footer = Footer.objects.filter(id=footer.id - 1)
        pre_footer.delete()
    return {'footer': footer}
