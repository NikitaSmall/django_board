from django import template
from simple_blog.models import Category

register = template.Library()


@register.inclusion_tag('includes/category_nav.html')
def category_nav():
    categories = Category.objects.order_by('-pub_date')
    return {'categories': categories}
