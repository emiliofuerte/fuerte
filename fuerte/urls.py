"""three_sentences URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from app import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('admin/', admin.site.urls, name='admin'),
    path('three/', views.three, name='three'),
    path('essays/', views.essays, name='essays'),
    path('coates/', views.coates, name='coates'),
    path('fake/', views.fake, name='fake'),
    path('sunrise/', views.sunrise, name='sunrise'),
    path('fragility/', views.fragility, name='fragility'),
    path('fence/', views.fence, name='fence'),
    path('food/', views.food, name='food'),
    path('upload_reviews/', views.upload_reviews, name='upload'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    
    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)