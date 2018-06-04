from django.conf.urls import url
from . import views

app_name = 'files'


'''
    TODO: refactor endpoints to reflect gist requirements
'''

urlpatterns = [
    url(r"^$", views.FileList.as_view(), name="all"),
    url(r"new/$", views.CreateFile.as_view(), name="create"),
    url(r"(?P<username>[-\w]+)/$", views.UserFiles.as_view(), name="for_user"),
    url(r"(?P<username>[-\w]+)/(?P<pk>\d+)/$", views.FileDetail.as_view(), name="single"),
    url(r"delete/(?P<pk>\d+)/$", views.DeleteFile.as_view(), name="delete"),
]
