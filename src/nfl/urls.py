from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='nfl_home'),
    url(r'^home/$', views.home, name='nfl_home'),
    url(r'^schedule/$', views.nfl_schedule, name='nfl_schedule'),
    url(r'^board/$', views.nfl_public_board, name='nfl_public_board'),
    url(r'^picked/$', views.nfl_picked_bet, name='nfl_picked_bet'),
    url(r'^confirm/$', views.nfl_confirm_bet, name='nfl_confirm_bet'),
    url(r'^create/$', views.nfl_create_bet, name='nfl_create_bet'),
]