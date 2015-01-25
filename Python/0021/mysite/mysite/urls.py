from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', 'addr_book.views.hello'),
    url(r'^time/', 'addr_book.views.current_time'),
    url(r'^insert', 'addr_book.views.insert'),
    url(r'^list', 'addr_book.views.list'),
)
