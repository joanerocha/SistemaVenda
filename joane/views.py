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
def inicio(request):
   return render(request, 'templates/base.html', {})

def index(request):
	try:
		if request.session['usuario'] == '':
			request.session['usuario'] = ''
	except:
		request.session['usuario'] = ''

	return render(request,'index.html',{
		'usuario': request.session['usuario']

		})

#@login_required(login_url='/entrar/')
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

#@login_required(login_url='/entrar/')
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

#@login_required(login_url='/entrar/')
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



#@login_required(login_url='/entrar/')
def excluircliente(request,id_cliente):
	cl = Cliente.cliente.get(pk = id_cliente)
	cmsg = ''
	nmsg1 = 0

	return render(request,'excluircliente.html',
	 	{
	 	'msg': cmsg,
	 	'nmsg': nmsg1
	 	})	

#@login_required(login_url='/entrar/')
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


#Fornecedor

def fornecedor(request):
	if request.method=='POST':
		amsg = []
		form = FormLocalizaFornecedor(request.POST)
		if form.is_valid():
			fnome = form.cleaned_data.get('nome')
			fn = Fornecedor.fornecedor.filter(nome__contains=fnome)
		else:
			fn = Fornecedor.fornecedor.all()
	else:
		fn = Fornecedor.fornecedor.all()
		form = FormLocalizaFornecedor()		
	return render(request,'fornecedor.html',{
		'form': form,
		'fornecedor': fn
		})

#@login_required(login_url='/entrar/')
def editarfornecedor(request, id_fornecedor):
	cmsg=''
	fn = Fornecedor.fornecedor.get(pk = id_fornecedor)
	if request.method == "POST":
		form = FormFornecedor(request.POST, request.FILES,instance=fn)
		if form.is_valid():
			print form
			form.save()
			cmsg = 'Dados salvos com sucesso.'

	else:
		form = FormFornecedor(instance=fn)
	return render(request,'editarfornecedor.html',
	 	{
	 	'fornecedor':fn,
	 	'msg': cmsg,
	 	'form': form
	 	})

#@login_required(login_url='/entrar/')
def incluirfornecedor(request):
	cmsg=''
	if request.method == "POST":
		form = FormFornecedor(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			cmsg = 'Dados salvos com sucesso.'

	else:
		form = FormFornecedor()
	return render(request,'incluirfornecedor.html',
	 	{
	 	'msg': cmsg,
	 	'form': form
	 	})



#@login_required(login_url='/entrar/')
def excluirfornecedor(request,id_fornecedor):
	fn = Fornecedor.fornecedor.get(pk = id_fornecedor)
	cmsg = ''
	nmsg1 = 0

	return render(request,'excluirfornecedor.html',
	 	{
	 	'msg': cmsg,
	 	'nmsg': nmsg1
	 	})	

#@login_required(login_url='/entrar/')
def fotofornecedor(request, id_fornecedor):
	import os, os.path
	if request.method == 'POST':
		form = FormFotoFornecedor(request.POST, request.FILES)
		if form.is_valid():
			fn = Fornecedor.fornecedor.get(pk = id_fornecedor)
			if os.path.isfile('.' + fn.foto.url):
				os.remove('.' + fn.foto.url)
			fn.foto = request.FILES['file']
			fn.save()

			return HttpResponseRedirect('/fornecedor/')
	else:
		form = FormFotoFornecedor()  

	fn = Fornecedor.fornecedor.all()

	return render_to_response(
        'fotofornecedor.html',
        {'fornecedor': fn, 'form': form},
        context_instance=RequestContext(request)
    )


#PRODUTO


def produto(request):
	if request.method=='POST':
		amsg = []
		form = FormLocalizaProduto(request.POST)
		if form.is_valid():
			pnome = form.cleaned_data.get('nome')
			pr = Produto.produto.filter(nome__contains=pnome)
		else:
			pr = Produto.produto.all()
	else:
		pr = Produto.produto.all()
		form = FormLocalizaProduto()		
	return render(request,'produto.html',{
		'form': form,
		'produto': pr
		})

#@login_required(login_url='/entrar/')
def editarproduto(request, id_produto):
	cmsg=''
	pr = Produto.produto.get(pk = id_produto)
	if request.method == "POST":
		form = FormProduto(request.POST, request.FILES,instance=pr)
		if form.is_valid():
			print form
			form.save()
			cmsg = 'Dados salvos com sucesso.'

	else:
		form = FormProduto(instance=pr)
	return render(request,'editarproduto.html',
	 	{
	 	'produto':pr,
	 	'msg': cmsg,
	 	'form': form
	 	})

#@login_required(login_url='/entrar/')
def incluirproduto(request):
	cmsg=''
	if request.method == "POST":
		form = FormProduto(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			cmsg = 'Dados salvos com sucesso.'

	else:
		form = FormProduto()
	return render(request,'incluirproduto.html',
	 	{
	 	'msg': cmsg,
	 	'form': form
	 	})



#@login_required(login_url='/entrar/')
def excluirproduto(request,id_produto):
	pr = Produto.produto.get(pk = id_produto)
	cmsg = ''
	nmsg1 = 0

	return render(request,'excluirproduto.html',
	 	{
	 	'msg': cmsg,
	 	'nmsg': nmsg1
	 	})	

#@login_required(login_url='/entrar/')
def fotoproduto(request, id_produto):
	import os, os.path
	if request.method == 'POST':
		form = FormFotoProduto(request.POST, request.FILES)
		if form.is_valid():
			pr = Produto.produto.get(pk = id_produto)
			if os.path.isfile('.' + pr.foto.url):
				os.remove('.' + pr.foto.url)
			pr.foto = request.FILES['file']
			pr.save()

			return HttpResponseRedirect('/produto/')
	else:
		form = FormFotoProduto()  

	pr = Produto.produto.all()

	return render_to_response(
        'fotoproduto.html',
        {'produto': pr, 'form': form},
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