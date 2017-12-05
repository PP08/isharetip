from django import template

register = template.Library()

@register.filter()
def genSlug(category):
    return str(category[0]).replace(' ', '-')