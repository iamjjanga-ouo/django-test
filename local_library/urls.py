"""local_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Use include() to paths from the catalog application
urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

# add URL maps to redirect the base URL to our application
# path()함수의 first parameter를 비워 놓으면 '/'을 의미.
urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]

# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

# Use static() to add url mapping to serve static files during deployment (only)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

'''
또는 다음과 같은 방식을 사용가능
urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
'''
