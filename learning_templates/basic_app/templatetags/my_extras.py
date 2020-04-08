from django import template

#customised filters
register = template.Library()

@register.filter(name='cut')
def cut(value, arg):

    """
    This cuts out all values of arg from the string
    """
    return value.replace(arg,'')

#WITHOUT DECORATORES
#register.filter('cut',cut) #first is the name given by you to your customised filter.
#second one is the name of the function defined.