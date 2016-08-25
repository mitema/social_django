from django.conf.urls import patterns, url
from social import views

urlpatterns = patterns('',
    # main page
    url(r'^$', views.index),
    # signup page
    url(r'^signup/$', views.signup),
    # register new user
    url(r'^register/$', views.register),
    # login page
    url(r'^login/$', views.login),
    # logout page
    url(r'^logout/$', views.logout),
    # members page
    url(r'^members/$', views.members),
    # friends page
    url(r'^friends/$', views.friends),
    # user profile edit page
    url(r'^profile/$', views.profile),
    # Ajax: check if user exists
    url(r'^checkuser/$', views.checkuser),
    # messages page
    url(r'^messages/$', views.messages),
    # message container
    url(r'^message_post/$', views.message_post),
)
