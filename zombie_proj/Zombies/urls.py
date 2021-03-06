from django.conf.urls import patterns, url
from Zombies import views

urlpatterns = patterns('',
        url(r'^$', views.home, name='home'),
        url(r'^leaderboards/$', views.leaderboard, name='leaderboards'),
        url(r'^start/', views.start, name = 'start'),
        url(r'^turn/(?P<turn>[A-Z]+)/(?P<pos>[0-9]+)/', views.turn, name = 'turn'),
        url(r'^user/(?P<user_name>[A-Za-z_/,-\.0-9]+)/$', views.userProfile, name = 'userProfile' ),
        url(r'^edit/$', views.edit_badges, name = 'badgeEditor'),
        url(r'^new/$', views.new, name = 'newGame'),
        url(r'^help/$', views.howto, name = 'help'),
        url(r'^player404/$', views.player404, name = 'player404')

        )
