from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^forum/(?P<subcategory_id>[0-9]+)/$', views.subcategory, name='forum'),
    url(r'^topic/(?P<topic_id>[0-9]+)/$', views.topic, name='topic'),
    url(r'^topic/(?P<topic_id>[0-9]+)/check$', views.topic_check, name='topic_check'),

    url(r'^forum/(?P<subcategory_id>[0-9]+)/topics/$', views.create_topic, name='new_topic'),
    url(r'^topic/(?P<topic_id>[0-9]+)/messages/$', views.create_message, name='new_message'),

    url(r'^loginpage/', views.loginpage_view, name='loginpage'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^signup/', views.signup_view, name='signup'),
]
