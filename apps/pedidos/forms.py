from django.forms import ModelForm
from django.db import models
from django import forms
from models import *

class Producto_Form(ModelForm):
	class Meta:
		model=Producto
class Pedidos_Form(forms.Form):
	class Meta:
		model=Pedidos
		exclude=['producto','id_sesion', 'estado']
