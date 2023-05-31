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
from django.urls import path
# import settings

from family_tree.views import family_member_view, family_form_view, home_view, images_view

urlpatterns = [
    path('', home_view, name="home"),
    path('images', images_view),
    path('home/', home_view),
    path('form/', family_form_view),
    path('member/', family_member_view),
    path('admin/', admin.site.urls),
]


# this code below is supposed to help f3tch images from the database and display on the gallery 
# page. not working at the moment as webpage displays alt message. fix TODO 


# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
