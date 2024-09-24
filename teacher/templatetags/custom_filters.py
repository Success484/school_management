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



@register.filter
def first_paragraph(text):
    if not text:
        return ''
    paragraphs = text.split('\n\n')  # Split by double newlines, which typically separates paragraphs
    return paragraphs[0] if paragraphs else ''
