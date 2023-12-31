"""
URL configuration for family project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
# import settings
from django.conf import settings
from django.conf.urls.static import static
from family_tree import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from family_tree.views import family_member_view, family_form_view, home_view, images, tree, home_base_view, login_view, logout_view, editprofile

urlpatterns = [
    path('home/', home_view, name="home"),
    path('images/', images, name="images"),
    path('', home_base_view, name="home_base"),
    # path('base/', home_base_view),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('form/', family_form_view),
    path('member/', family_member_view, name='member'),
    path('admin/', admin.site.urls),
    path('check_family_member/', views.check_family_member, name='check_family_member'),
    # path('__reload__/', include('django_browser_reload.urls')), #, namespace='django_browser_reload' for tailwindcss
    path('tree/', tree, name='tree'),
    path('editprofile/', editprofile, name='editprofile'),
    path('save_details/', views.save_details, name='save_details'),
]


# this code below is supposed to help f3tch images from the database and display on the gallery 
# page. not working at the moment as webpage displays alt message. fix TODO 


# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

