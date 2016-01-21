from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import allauth


admin.autodiscover()
 
from tastypie.api import Api
#from polls.api import PollResource, ChoiceResource

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'alefone_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$','profiles.views.home', name='home'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$','profiles.views.home',name='home'),
    url(r'^about','profiles.views.about', name='about'),
    url(r'^profile','profiles.views.user_profile', name='profile'),
    url(r'^checkout','checkout.views.checkout', name='checkout'),
    url(r'^contact','contact.views.home',name='contact'),
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^oauth2/', include('provider.oauth2.urls', namespace = 'oauth2')),
#    url(r'^api/', include(v1_api.urls)),
) + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
