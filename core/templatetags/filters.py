from django import template

register = template.Library()


@register.filter()
def get_class(session_key, pk) -> str:
    if session_key.get(f'sweat_number{pk}', False):
        return 'fa fa-heart'
    else:
        return 'fa fa-heart-o'
