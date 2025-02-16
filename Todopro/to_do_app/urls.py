from django.urls import path
from . import views



urlpatterns = [
    path("", views.user_login,name='login'),
    path('home/',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('delete-task/<str:name>/',views.delete,name='delete'),
    path('update-task/<str:name>',views.update,name='update'),
    path('logout',views.user_logout,name = 'logout')
]
