from django import template

register = template.Library()

@register.filter(name='cut')

def cut(value, arg):
    """
        This function cuts the word
    """

    return value.replace(arg ,'')

#register.filter('cut',cut)