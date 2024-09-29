"""
URL configuration for clowiz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('cloth_list', views.cloth_list),
    #path('save_cloth', views.save_cloth),
    path('get_csrf_token', views.get_csrf_token),
    path('',views.user_login_page, name='login'),
    path('dashboard', views.home, name='dashboard'),
    path('login', views.user_login_page, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('register', views.user_register_page, name='register'),
    path('new_cloth', views.new_cloth_page, name='new_cloth'),
    path('view_wardrobe', views.view_wardrobe, name='view_wardrobe'),
    path('wardrobe_usage', views.wardrobe_usage, name='wardrobe_usage'),
    path('sustainability', views.sustainability, name='sustainability'),
    path('outfit_combo', views.outfit_combo, name='outfit_combo'),
    path('donate', views.donate, name='donate'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)