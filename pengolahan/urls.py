"""pengolahan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from pengolahan_app.views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('info/', info, name='info'),
    path('sebaran/', sebaran, name='sebaran'),
    path('tambahsebaran/', tambahsebaran),
    path('sebaran/updatesebaran/<int:kl>', updatesebaran, name='update2'),
    path('sebaran/deletesebaran/<int:kl>', deletesebaran, name='delete2'),
    path('berita/', berita),
    path('tambahberita/', tambahberita),
    path('berita/updateberita/<int:id>', updateberita, name='update'),
    path('berita/deleteberita/<int:id>', deleteberita, name='delete'),
    path('masuk/', LoginView.as_view(), name='masuk'),
    path('logout/', LogoutView.as_view(next_page='info'), name='logout'),
    path('signup/', signup, name='signup'),
    
]
