from django import template
register = template.Library()

@register.filter
def genSlug(title):
    return title.replace(' ', '-')