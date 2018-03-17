from django.conf.urls import url
from baseten.views import homepage, about_science, about_math, applications


urlpatterns = [
    url(r'^$', homepage, name = 'homepage'),
    url(r'o-nauci/$', about_science, name = 'about_science'),
    url(r'o-matematici/$', about_math, name = 'about_math'),
    url(r'primene-matematike/$', applications, name = 'applications'),
]
