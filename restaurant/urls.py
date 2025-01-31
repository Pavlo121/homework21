from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('home/', views.home, name='home'),  # Home page route
    path('about/', views.about, name='about'),
    path('book/', views.book, name='book'),
    path('menu/', views.menu, name='menu'),
    path('menu_item/<int:pk>/', views.display_menu_item, name='menu_item'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]