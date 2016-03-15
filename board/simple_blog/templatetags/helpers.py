from django import template
from simple_blog.models import Category

import imghdr

register = template.Library()


@register.inclusion_tag('includes/category_nav.html')
def category_nav():
    categories = Category.objects.order_by('-pub_date')
    return {'categories': categories}


@register.inclusion_tag('includes/image_check.html')
def image_check(image):
    if image:
        img_path = image.url
        file_type = imghdr.what(image.path)

        if file_type == 'png' or file_type == 'jpeg' or file_type == 'gif' or file_type == 'jpg':
            return {'image': img_path}

    return {'image': None}
