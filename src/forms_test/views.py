from django.shortcuts import render

from .forms import TestForm

def home(request):
    initial_data =  {
        "un_texto":"Texto inicial",
        "booleano": True,
        #"entero":100,
        #"correo":"test@test.com"
    }
    form = TestForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "forms.html", {"form":form})
