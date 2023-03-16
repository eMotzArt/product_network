from django.urls import path
from core import views

urlpatterns = [
    path('reg', views.RegisterAgentView.as_view(), name='register agent'),
    path('login', views.LoginLogoutView.as_view(), name='login'),
    path('logout', views.LoginLogoutView.as_view(), name='logout')
]
