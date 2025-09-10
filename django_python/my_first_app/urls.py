"""
URL configuration for django_python project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.http import HttpResponse
from django.urls import path
from my_first_app.models import Car
from my_first_app.views import my_view, car_datail, my_test_view, CarListView

urlpatterns = [
    #path("listado", my_test_view),
    path("listado", CarListView.as_view()), # Usando vista basada en clases
    path("detalle/<int:id>", car_datail),
    path("marcas/<str:id>", my_test_view),
    path("colores/<str:color_name>", my_test_view),
]
