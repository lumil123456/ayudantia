from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^$', pagina_index),
	url(r'^usuarios/$',usuarios), 
	url(r'^productos/$',productos), 
	url(r'^realizar_pedido/$',realizar_pedido),  
	url(r'^listar_productos/$',listar_productos),
	url(r'^modificar/(?P<id>\d+)/$',modificar_producto,name='modificar_producto'),
	url(r'^eliminarpedido/(?P<id>\d+)/$',eliminar_pedido,name='eliminar_pedido'),
)
