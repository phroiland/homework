from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .  import views


app_name = 'login'


'''
    TODO: refactor endpoints to reflect gist requirements
'''

urlpatterns = [
    url(r'login/$', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    url(r'logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'register/$', views.Register.as_view(), name='register')
]