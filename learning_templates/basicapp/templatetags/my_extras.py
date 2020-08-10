from django import template

register = template.Library()

# @register.filter(name='but')
def but(value,arg):
    """
    This cuts all values of "arg" from teh string
    """
    return value.replace(arg,'')

register.filter('but',but)
