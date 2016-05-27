# -*- coding:utf-8 -*-
from django import forms
from django.forms import CharField, Form, PasswordInput,ModelForm
from django.contrib.admin import widgets         
from django.contrib.auth.models import User
from joane.models import *
from django.contrib.admin.widgets import AdminFileWidget

class FormLogin(forms.Form):
	usuario=forms.CharField(label='Usuário',required=True)
	senha=forms.CharField(label='Senha', required=True)

class FormLocalizaCliente(forms.Form):
	nome = forms.CharField(label='Nome', required=True, widget=forms.TextInput(attrs={'placeholder': 'Pesquisar'}))

class FormFotoCliente(forms.Form):
	file = forms.FileField(label='Buscar foto')  

class FormCliente(ModelForm):
	class Meta:
		model=Cliente
		fields=['nome',]



#Fornecedor

class FormLocalizaFornecedor(forms.Form):
	fnome = forms.CharField(label='Nome', required=True, widget=forms.TextInput(attrs={'placeholder': 'Pesquisar'}))

class FormFotoFornecedor(forms.Form):
	file = forms.FileField(label='Buscar foto')  

class FormFornecedor(ModelForm):
	class Meta:
		model=Fornecedor
		fields=['fnome',]



#Produto

class FormLocalizaProduto(forms.Form):
	pnome = forms.CharField(label='Nome', required=True, widget=forms.TextInput(attrs={'placeholder': 'Pesquisar'}))

class FormFotoProduto(forms.Form):
	file = forms.FileField(label='Buscar foto')  

class FormProduto(ModelForm):
	class Meta:
		model=Produto
		fields=['pnome',]	
