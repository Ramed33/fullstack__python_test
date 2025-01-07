from django.shortcuts import render

from datetime import datetime

from django.contrib import messages

def test_view(request):
    my_list = ["Mouse", "Laptop", "Teclado", "Audífonos", "Multicontactod", "Celular"]
    context = {
        "view_title":"MI TÍTULO INCREÍBLE",
        "my_number":"675",
        "my_number2":2000,
        "today": datetime.now().today(),
        "my_list": my_list
    }
    template = "test_templates/detail-view.html" #<----------

    messages.add_message(request, messages.INFO, 'Mensaje de Prueba 1')
    messages.add_message(request, messages.INFO, 'Mensaje de Prueba 2')
    return render(request, template, context)
