from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    
    # Park View
    url(r'^park/(?P<pk>\d+)/$', views.ParkView.as_view(), name='park'),

    
    
    
    # ex: /polls/5/results/
    # url(r'^(?P<pk>\d+)/results/$', views.ResultView.as_view(), name='results'),

    # make the url below work. 
#    url(r'^(?P<poll_id>\d+)/results/(?P<choice>[\s\w\d-]+)/$', 'polls.views.results', name='results'),
    
    # ex: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    
    # my results view with choice
    url(r'^(?P<poll_id>\d+)/results/(?P<choice_id>\d+)/$', views.results, name='results'),

    # write-in url
#    url(r'writein/(/d*)/$', views.writein, name='writein'),

)

