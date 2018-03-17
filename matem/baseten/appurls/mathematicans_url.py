from django.conf.urls import url
from baseten.views import mathematicians, input_mat, output_mat, delete_mat

urlpatterns = [
    url(r'^$', mathematicians, name = 'mathematicians'),
    url(r'^input-mathematician/$', input_mat, name = 'input_mathematician'),
    url(r'^read-mathematician/$', output_mat, name = 'read_mathematician'),
    url(r'^delete-mathematician/$', delete_mat, name = 'delete_mathematician'),
]
