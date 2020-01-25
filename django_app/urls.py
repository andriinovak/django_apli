"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from core.views import landing_page_view, info_about_me, contact_us_view, feedbacks, subjects_page, subject_item_view
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page_view),
    path('about_us/', info_about_me),
    path('contact_us/', contact_us_view),
    path('subjects/<str:subject_name>/', subject_item_view, name='subject'),
    path('feedbacks-for-all-users/', feedbacks, name='feedbacks'),
    path('feedbacks/', RedirectView.as_view(url='feedbacks')),
    path('subjects/', subjects_page)
    ]
