from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('register/', views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name="task/login.html") , name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="task/logout.html") , name="logout"),
    path('task/', views.add_task, name="add_task"),
]
