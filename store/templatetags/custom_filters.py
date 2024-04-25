from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return float(value) * int(arg)  # Convertir arg en entier pour la quantité
    except (ValueError, TypeError):
        return value
