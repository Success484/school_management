from django import template
import calendar

register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)



@register.filter
def get_num_days_in_month(month, year):
    return calendar.monthrange(year, month)[1]


@register.filter
def get_month_name(month_number):
    """Converts a month number to its name."""
    return calendar.month_name[month_number]