from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})

def times(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0