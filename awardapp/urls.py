from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$',views.home,name='homePage'),
    url(r'^upload$',views.upload,name='upload'),
    url(r'^ratecontent/(\d+)',views.add_content, name='ratecontent'),
    url(r'^ratedesign/(\d+)',views.add_design, name='ratedesign'),
    url(r'^rateusability/(\d+)',views.add_usability, name='rateusability'),
    url(r'^profile/(\d+)',views.profile,name='profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'^api/project/$', views.ProjectList.as_view()),
    url(r'api/project/project-id/(?P<pk>[0-9]+)/$',views.ProjectDescription.as_view()),
    url(r'api/profile/profile-id/(?P<pk>[0-9]+)/$',views.ProfileDescription.as_view()),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)