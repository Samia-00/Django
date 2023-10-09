from django import template

register = template.Library()
@register.filter(name='cut')
def cut(value,arg):
    """
    THIS CUTS OUT ALL VALUES OF ARGS FROM THE STRING
    :param value:
    :param arg:
    :return:
    """
    return value.replace(arg,'')
register.filter('cut',cut)