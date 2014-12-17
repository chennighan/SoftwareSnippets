from django import template
from pygments.formatters import HtmlFormatter

register = template.Library()

@register.simple_tag
def pygment_style():
  return HtmlFormatter().get_style_defs('.highlight')