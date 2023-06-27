from django.urls import path
from . import views

urlpatterns = [
    path('',views.cargarInicio),
    path('inicio',views.cargarInicio),
    path('productos',views.cargarProductos),
    path('sobre_nosotros',views.cargarSobre),
    path('login',views.cargarLogin),

    path('agregarPro',views.cargarAgregar),
    path('editarPro/<sku>',views.cargarEditarProducto),
    path('editarProductoForm',views.editarProductoForm),
    path('eliminarProducto/<sku>',views.eliminarProducto),
    path('carrito', views.carrito)
    

]