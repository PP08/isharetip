from django import template

register = template.Library()

@register.filter()
def genSlug(category):
    return category.replace(' ', '-')