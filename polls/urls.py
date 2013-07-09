from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<pk>\d+)/results/$', views.ResultView.as_view(), name='results'),

    # make the url below work.
    # url(r'^(?P<pk>\d+)/results/(?P<choice>[\s\w\d-]+)/$', 'polls.views.results', name='results'),
    
    # ex: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    # ex: 
#    url(r'^(?P<pk>\d+)/page/$', views.PageView.as_view(), name='page'),
    #
#    url(r'^(?P<page_name>[^/]+)/$', views.view_page, name='page'),
    #
#    url(r'^(?P<page_name>[^/]+)/edit/$', views.edit_page, name='edit'),
    #
#    url(r'^(?P<page_name>[^/]+)/save/$', views.save_page, name='save'),
)
