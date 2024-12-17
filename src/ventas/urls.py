from django.urls import path

from ventas import views

urlpatterns = [
    path("carrito", views.VentasCarritoView.as_view(), name="ventas-carrito"),
    path("product-list", views.VentasProductListView.as_view(), name="ventas-product-list"),
    path("pedido", views.VentasPedidoView.as_view(), name="ventas-pedido"),
    path("recomendado", views.VentasRecomendadoView.as_view(), name="ventas-recomendado"),

]
