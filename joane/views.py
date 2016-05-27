# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, logout, login

from joane.models import *
from joane.forms import *

# Create your views here.
#def inicio(request):
 #   return render(request, 'templates/base.html', {})

def index(request):
	try:
		if request.session['usuario'] == '':
			request.session['usuario'] = ''
	except:
		request.session['usuario'] = ''

	return render(request,'index.html',{
		'usuario': request.session['usuario']

		})

@login_required(login_url='/entrar/')
def cliente(request):
	if request.method=='POST':
		amsg = []
		form = FormLocalizaCliente(request.POST)
		if form.is_valid():
			cnome = form.cleaned_data.get('nome')
			cl = Cliente.cliente.filter(nome__contains=cnome)
		else:
			cl = Cliente.cliente.all()
	else:
		cl = Cliente.cliente.all()
		form = FormLocalizaCliente()		
	return render(request,'cliente.html',{
		'form': form,
		'cliente': cl
		})

@login_required(login_url='/entrar/')
def editarcliente(request, id_cliente):
	cmsg=''
	cl = Cliente.cliente.get(pk = id_cliente)
	if request.method == "POST":
		form = FormCliente(request.POST, request.FILES,instance=cl)
		if form.is_valid():
			print form
			form.save()
			cmsg = 'Dados salvos com sucesso.'

	else:
		form = FormCliente(instance=cl)
	return render(request,'editarcliente.html',
	 	{
	 	'cliente':cl,
	 	'msg': cmsg,
	 	'form': form
	 	})

@login_required(login_url='/entrar/')
def incluircliente(request):
	cmsg=''
	if request.method == "POST":
		form = FormCliente(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			cmsg = 'Dados salvos com sucesso.'

	else:
		form = FormCliente()
	return render(request,'incluircliente.html',
	 	{
	 	'msg': cmsg,
	 	'form': form
	 	})



@login_required(login_url='/entrar/')
def excluircliente(request,id_cliente):
	cl = Cliente.cliente.get(pk = id_cliente)
	cmsg = ''
	nmsg1 = 0

	return render(request,'excluircliente.html',
	 	{
	 	'msg': cmsg,
	 	'nmsg': nmsg1
	 	})	




@login_required(login_url='/entrar/')
def fotocliente(request, id_cliente):
	import os, os.path
	if request.method == 'POST':
		form = FormFotoCliente(request.POST, request.FILES)
		if form.is_valid():
			cl = Cliente.cliente.get(pk = id_cliente)
			if os.path.isfile('.' + cl.foto.url):
				os.remove('.' + cl.foto.url)
			cl.foto = request.FILES['file']
			cl.save()

			return HttpResponseRedirect('/cliente/')
	else:
		form = FormFotoCliente()  

	cl = Cliente.cliente.all()

	return render_to_response(
        'fotocliente.html',
        {'cliente': cl, 'form': form},
        context_instance=RequestContext(request)
    )

@csrf_exempt
def entrar(request):
	if request.method=='POST':
		form = FormLogin(request.POST)
		if form.is_valid():
			cusuario = form.cleaned_data.get('usuario')
			csenha = form.cleaned_data.get('senha')

			user = authenticate(username=cusuario, password=csenha)
			if user is not None:
				if user.is_active:
					login(request, user)
					request.session['usuario'] = cusuario
					return HttpResponseRedirect('/') 
				else:
					form = FormLogin()
					return render(request, 'entrar.html',{
						'usuario': user
						}) 
			else:
				form = FormLogin()
				return render(request, 'entrar.html',{
					'usuario': user,
					'form': form
						})  

	else:
		form = FormLogin()
	return render(request,'entrar.html', 
		{
		'usuario': True,
		'form': form
		})

@csrf_exempt
def sair(request):
	logout(request)
	request.session.flush()
	return HttpResponseRedirect('/')