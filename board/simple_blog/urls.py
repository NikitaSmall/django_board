from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^forum/(?P<pk>[0-9]+)/$', views.SubcategoryView.as_view(), name='forum'),
    url(r'^topic/(?P<pk>[0-9]+)/$', views.TopicView.as_view(), name='topic'),

    url(r'^forum/(?P<subcategory_id>[0-9]+)/topics/$', views.create_topic, name='new_topic'),
    url(r'^topic/(?P<topic_id>[0-9]+)/messages$', views.create_message, name='new_message'),
]
