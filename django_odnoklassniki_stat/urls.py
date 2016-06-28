from django.conf.urls import patterns, include, url
from django.contrib import admin
from odnoklassniki_stats import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'untitled1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', views.call),
    url(r'^apiddd/', views.call),
)
