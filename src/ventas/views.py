from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http.request import HttpRequest as HttpRequest
from django.views.generic import TemplateView
from django.shortcuts import render

class VentasProductListView(LoginRequiredMixin, TemplateView):
    template_name = "ventas/product-list.html"

    def dispatch(self, *args, **kwargs):
        user = self.request.user
        if not user.is_staff:
            return HttpResponse("No permitido", status=401)
        return super(VentasProductListView, self).dispatch(*args, **kwargs)
    
    def get_context_data(self, *args, **kwargs):
        return super(VentasProductListView, self).get_context_data(*args, **kwargs)

class VentasCarritoView(LoginRequiredMixin, TemplateView):
    template_name = "ventas/carrito.html"

    def dispatch(self, *args, **kwargs):
        user = self.request.user
        if not user.is_staff:
            return HttpResponse("No permitido", status=401)
        return super(VentasCarritoView, self).dispatch(*args, **kwargs)
    
    def get_context_data(self, *args, **kwargs):
        return super(VentasCarritoView, self).get_context_data(*args, **kwargs)
    
class VentasPedidoView(LoginRequiredMixin, TemplateView):
    template_name = "ventas/pedido.html"

    def dispatch(self, *args, **kwargs):
        user = self.request.user
        if not user.is_staff:
            return HttpResponse("No permitido", status=401)
        return super(VentasPedidoView, self).dispatch(*args, **kwargs)
    
    def get_context_data(self, *args, **kwargs):
        return super(VentasPedidoView, self).get_context_data(*args, **kwargs)
    
class VentasRecomendadoView(LoginRequiredMixin, TemplateView):
    template_name = "ventas/recomendado.html"

    def dispatch(self, *args, **kwargs):
        user = self.request.user
        if not user.is_staff:
            return HttpResponse("No permitido", status=401)
        return super(VentasRecomendadoView, self).dispatch(*args, **kwargs)
    
    def get_context_data(self, *args, **kwargs):
        return super(VentasRecomendadoView, self).get_context_data(*args, **kwargs)