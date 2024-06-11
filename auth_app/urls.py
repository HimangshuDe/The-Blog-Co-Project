from django.urls import path

from auth_app import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('account/', views.accounts_view, name='account'),
    path('delete/', views.del_user, name='delete'),
    path('logout/', views.user_logout, name='logout'),
]
