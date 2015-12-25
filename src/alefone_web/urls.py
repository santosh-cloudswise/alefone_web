from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'alefone_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$','profiles.views.home', name='home'),
    url(r'^$','profiles.views.home',name='home'),
    url(r'^about','profiles.views.about', name='about'),
    url(r'^contact','contact.views.home',name='contact'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
