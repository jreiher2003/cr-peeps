from dateutil.parser import parse as parse_date 
from django import template

register = template.Library()

@register.filter
def dateify(value):
    return parse_date(value)