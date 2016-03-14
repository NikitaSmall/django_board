from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^forum/(?P<subcategory_id>[0-9]+)/$', views.subcategory, name='forum'),
]
