from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views
# from .forms import LoginForm

urlpatterns = [
    path('', views.index, name='index'),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
     path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup_user, name='signup'),
]

