from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from models import *
from forms import *
import hashlib
import datetime
# Create your views here.
def pagina_index(request):
	return render_to_response("blog/index.html",{},context_instance=RequestContext(request))

def usurios(request):
	usuarios=User.objects.all()
	producto=Producto.objects.all()
	return render_to_response("blog/usuarios.html",{"usuarios":usuarios})
def registrarProducto(request):
	if request.method=="POST":
		print "registrar"
		form=Producto_Form(request.POST)
		print "formulario %s"%(form)
		if(form.is_valid()):
			print request.POST
			form.save();
			return HttpResponseRedirect("/productos/ultimoregistro/")
	form=Producto_Form()
	return render_to_response("producto/registrar.html",{"form":form},RequestContext(request))
def productos(request):
	lista_productos=Producto.objects.all()
	return render_to_response("blog/producto.html",{"lista_productos":lista_productos},context_instance=RequestContext(request))

def realizar_pedido(request):
	if request.user.is_authenticated():
        id_sesion=request.session["id_sesion"]
        carr=Carrito.objects.filter(id_sesion=id_sesion)
        return render_to_response("blog/realizar_pedido.html",{'carr':carr},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect("/usuario/ingresar/")
def registrar_nuevo_pedido(request):
	if request.method=="POST":
		print "registrar"
		form=Pedidos_Form(request.POST)
		print "formulario %s"%(form)
		if(form.is_valid()):
			print request.POST
			form.save();
			return HttpResponseRedirect("/producto/ultimoregistro/")
	form=Pedidos_Form()
	return render_to_response("producto/registrar_nuevo_pedido.html",{"form":form},RequestContext(request))

def listar_pedido_productos(request,id):
	producto=Producto.objects.get(id=int(id))
	return render_to_response("blog/lista_productos.html",{"producto":producto},context_instance=RequestContext(request))

def modificar_producto(request):
	producto=get_object_or_404(mproducto, pk=id)
	if request.method=="POST":
		fpregunta=Producto_Form(request.POST, instance=producto)
		if fproducto.is_valid():
			fproducto.save()
			return HttpResponse("producto modificada")
	else:
		fproducto=Producto_Form(instance=producto)
	return render_to_response("blog/modificar_producto.html",{"fpregunta":fpregunta},RequestContext(request))
#def modificar_producto(request):
#	producto=Producto.objects.get(id=id)
#	if request.method=="POST":
#		form=Producto_Form(request.POST)
#		if form.is_valid():
#			producto.save()
#			return render_to_response("proyectos/modificar.html",{"form":form},RequestContext(request))
#	form=Producto_Form(instance=producto)
#	return render_to_response("producto/modificar_producto.html",{"form":form},RequestContext(request))

def eliminar_pedido(request,id):
	elim=pedido.objects.get(pk=id)
	borrar=elim.delete()
	updateprecio(request.session["idPro"])
	return render_to_response("/blog/eliminar_pedido/")
