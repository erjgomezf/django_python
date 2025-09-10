from django.shortcuts import render
from django.http import HttpResponse
from my_first_app.models import Car
from django.views.generic.base import TemplateView

# Create your views here.
def my_view(request):
    car_list = [
        {"title": "Toyota"},
        {"title": "Honda"},
        {"title": "Ford"},
    ]
    context = {
        "car_list": car_list
    }
    return render(request, "my_first_app/car_list.html", context)

class CarListView(TemplateView):
    """
    Vista basada en clases
    Muestra una lista de carros
    """
    template_name = "my_first_app/car_list.html"

    def get_context_data(self) -> dict:
        """
        Retorna el contexto para la plantilla
        :return: dict
        :rtype: dict
        """
        context = super().get_context_data() # Llama al método de la clase padre
        
        car_list = [
            {"title": "Toyota"},
            {"title": "Honda"},
            {"title": "Ford"},
            {"title": "Suzuki"},
        ]
        context = {
            "car_list": car_list
        }
        return context

def my_test_view(request, *arg, **kwargs):
    print(arg)
    print(kwargs)
    return HttpResponse(f"hola mundo {arg} {kwargs}")

def car_datail(request, id):
    car = Car.objects.get(id=id)
    return HttpResponse(f"Detalle del carro con ID: {car.id}: marca: {car.title}, color: {car.colors}, año: {car.year}") 