from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
import os
from django.conf import settings

import json
from django.http import HttpResponse


# Create your views here.

def cargarInicio(request):
    return render(request, "inicio.html")

def cargarProductos(request):
    return render(request, "productos.html")

def cargarSobre(request):
    return render(request, "sobre_nosotros.html")

def cargarLogin(request):
    
    return render(request, "login.html")

@login_required
def cargarAgregar(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request,"agregarPro.html",{"cate":categorias, "prod":productos})

def cargarEditarProducto(request,sku):
    productos = Producto.objects.get(sku = sku)
    categorias = Categoria.objects.all()

    cateId = productos.categoria_id

    productoCategoria = Categoria.objects.get(categoria_id = cateId.categoria_id).categoria_id

    return render(request,"editarPro.html",{"prod":productos, "cate":categorias,"categoriaId":productoCategoria})


def cargarEditarProducto(request,sku):
    productos = Producto.objects.get(sku = sku)
    categorias = Categoria.objects.all()

    cateId = productos.categoria_id

    productoCategoria = Categoria.objects.get(categoria_id = cateId.categoria_id).categoria_id

    return render(request,"editarPro.html",{"prod":productos, "cate":categorias,"categoriaId":productoCategoria})



def editarProductoForm(request):
    v_sku = request.POST['txtSku']
    productoBD = Producto.objects.get(sku = v_sku)
    v_nombre = request.POST['txtNombre']
    v_descripcion = request.POST['txtDescripcion']
    v_stock = request.POST['txtStock']
    v_precio = request.POST['txtPrecio']
    if request.POST['fechaVencimientoSel'] == "":
        v_fecha_vencimiento = None
    else:
        v_fecha_vencimiento = request.POST['fechaVencimientoSel']
    v_categoria = Categoria.objects.get(categoria_id = request.POST['cmbCategoria'])


    try:
        v_image = request.FILES['txtImg']
        ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(productoBD.image_url))
        os.remove(ruta_imagen)
    except:
        v_image = productoBD.image_url


    productoBD.nombre = v_nombre
    productoBD.descripcion = v_descripcion
    productoBD.stock = v_stock
    productoBD.precio = v_precio
    productoBD.fecha_vencimiento = v_fecha_vencimiento
    productoBD.image_url = v_image
    productoBD.categoria_id = v_categoria


    productoBD.save()
    return redirect('/agregarPro')

def eliminarProducto(request,sku):
    print("ELIMINAR PRODUCTO",sku)
    producto = Producto.objects.get(sku = sku)
    ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(producto.image_url))
    os.remove(ruta_imagen)
    producto.delete()
    return redirect('/agregarPro')

def carrito(request):
    print('carrito',request.body)
    data = json.loads(request.body)
    for p in data:
        print('SKU',p['sku'])
        print('CANTIDAD',p['cantidad'])
    return HttpResponse('OK')
