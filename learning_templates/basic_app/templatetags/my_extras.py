from django import template

register = template.Library()


# Option1:
# def cut(value, arg):
#     """
#     This cuts out all values of "arg" from the string!
#     """
#     return value.replace(arg, "")
#
#
# register.filter('cut', cut)


# Option2: python decorator
@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg, "")
