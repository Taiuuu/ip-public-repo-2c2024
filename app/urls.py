from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.index_page, name='index-page'),
    path('login/', views.index_page, name='login'),
    path('home/', views.home, name='home'),
    path('buscar/', views.search, name='buscar'),

    path('favourites/', views.getAllFavouritesByUser, name='favoritos'),
    path('favourites/add/', views.saveFavourite, name='agregar-favorito'),
    path('favourites/delete/', views.deleteFavourite, name='borrar-favorito'),

    path('exit/', views.exit, name='exit'),

    #iniciar sesion
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    #register
    path('register/', views.register, name='register'),
]