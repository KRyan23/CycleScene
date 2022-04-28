from django import template
from django.urls import reverse

register = template.Library()

#Register simple template tag that brings the user to the correct page section
@register.simple_tag
def section(url_name, section_id):
    return reverse(url_name) + '#' + section_id
