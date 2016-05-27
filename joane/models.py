# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

#Cliente

class Cliente(models.Model):
	nome = models.CharField(verbose_name = 'Nome', max_length = 100)
	foto = models.ImageField(upload_to = 'cliente/', height_field = None, width_field = None, max_length = 100, blank = True, null = True, default = 'cliente/no_foto.jpg')
	
	cliente = models.Manager()
	id = models.AutoField(primary_key = True)

	def __str__(self):
		return self.nome

class Documento(models.Model):
	cliente = models.ForeignKey(Cliente)
	numeroDoc = models.DecimalField(verbose_name = 'Número Documento', max_digits = 15, decimal_places = 2, default = 0, primary_key = 'True')
	tipo = models.CharField(verbose_name = 'Tipo Documento', max_length = 100)
	emissao = models.DateField(verbose_name = 'Emissão')
	vencimento = models.DateField(verbose_name = 'Vencimento')
	docAtivo = models.BooleanField(verbose_name = 'Ativo')

	def __str__(self):
		return self.tipo

class Endereco(models.Model):
	cliente = models.ForeignKey(Cliente)
	cep = models.DecimalField(verbose_name = 'CEP',max_digits = 8, decimal_places = 2, default=0)
	tipo = models.CharField(verbose_name = 'Tipo', max_length = 100)
	descricao = models.CharField(verbose_name = 'Descrição', max_length = 300)
	complemento = models.CharField(verbose_name = 'Complemento', max_length = 100)
	numero = models.DecimalField(verbose_name = 'Número', max_digits = 15, decimal_places = 2, default=0)
	ativo = models.BooleanField(verbose_name = 'Ativo') 
	id = models.AutoField(primary_key = True)

	def __str__ (self):
		return self.tipo

class Email(models.Model):
	cliente = models.ForeignKey(Cliente)
	descricaoEmail = models.CharField(verbose_name = 'Descirção do Email', max_length = 100)
	emailAtivo = models.BooleanField(verbose_name = 'Ativo')
	id = models.AutoField(primary_key = True)

	def __str__(self):
		return self.descricaoEmail


#Fornecedor

class Fornecedor(models.Model):
	fnome = models.CharField(verbose_name = 'Nome', max_length = 100)
	ffoto = models.ImageField(upload_to = 'fornecedor/', height_field = None, width_field = None, max_length = 100, blank = True, null = True, default = 'cliente/no_foto.jpg')
	
	fornecedor = models.Manager()
	id = models.AutoField(primary_key = True)

	def __str__(self):
		return self.fnome

#Documento

class FDocumento(models.Model):
	fornecedor = models.ForeignKey(Fornecedor)
	fnumeroDoc = models.DecimalField(verbose_name = 'Número Documento', max_digits = 15, decimal_places = 2, default = 0, primary_key = 'True')
	ftipo = models.CharField(verbose_name = 'Tipo Documento', max_length = 100)
	femissao = models.DateField(verbose_name = 'Emissão')
	fvencimento = models.DateField(verbose_name = 'Vencimento')
	fdocAtivo = models.BooleanField(verbose_name = 'Ativo')

	def __str__(self):
		return self.ftipo

#Endereco

class FEndereco(models.Model):
	fornecedor = models.ForeignKey(Fornecedor)
	fcep = models.DecimalField(verbose_name = 'CEP',max_digits = 8, decimal_places = 2, default=0)
	ftipo = models.CharField(verbose_name = 'Tipo', max_length = 100)
	fdescricao = models.CharField(verbose_name = 'Descrição', max_length = 300)
	fcomplemento = models.CharField(verbose_name = 'Complemento', max_length = 100)
	fnumero = models.DecimalField(verbose_name = 'Número', max_digits = 15, decimal_places = 2, default=0)
	fativo = models.BooleanField(verbose_name = 'Ativo') 
	id = models.AutoField(primary_key = True)

	def __str__ (self):
		return self.ftipo

#Email

class FEmail(models.Model):
	fornecedor = models.ForeignKey(Fornecedor)
	fdescricaoEmail = models.CharField(verbose_name = 'Descirção do Email', max_length = 100)
	femailAtivo = models.BooleanField(verbose_name = 'Ativo')
	id = models.AutoField(primary_key = True)

	def __str__(self):
		return self.fdescricaoEmail

#Unidade

class Unidade(models.Model):
	descricao = models.CharField(verbose_name = 'Descrição da Unidade', max_length = 100)
	fator = models.DecimalField(verbose_name = 'Fator', max_digits = 15, decimal_places = 2, default = 0)

	def __str__(self):
		return self.descricao

# Produto

class Produto(models.Model):
	unidade = models.ForeignKey(Unidade)
	pnome = models.CharField(verbose_name = 'Nome', max_length = 100)
	pfoto = models.ImageField(upload_to = 'produto/', height_field = None, width_field = None, max_length = 100, blank = True, null = True, default = 'produto/no_foto.jpg')
	descricao = models.CharField(verbose_name = 'Descrição do Produto', max_length = 100)
	estoque = models.DecimalField(verbose_name = 'Estoque', max_digits = 15, decimal_places = 2, default = 0)

	produto = models.Manager()
	id = models.AutoField(primary_key = True)

	def __str__(self):
		return self.pnome
	#pega chave

#Item

class Item(models.Model):
	produto = models.ForeignKey(Produto)
	qtd = models.DecimalField(verbose_name = 'Quantidade', max_digits = 15, decimal_places = 2, default = 0)
	valor = models.DecimalField(verbose_name = 'Valor', max_digits = 15, decimal_places = 2, default = 0)

	#pega chave, não tem chave estrangeira

#Pedido

class Pedido(models.Model):
	item = models.ForeignKey(Item)

	#pega chave

#Venda

class Venda(models.Model):
	intem = models.ForeignKey(Item) #pega chave

#Financeiro

class Financeiro(models.Model):
	entidade = models.CharField(verbose_name = 'Entidade', max_length = 100)
	parcela = models.DecimalField(verbose_name = 'Parcela', max_digits = 15, decimal_places = 2, default = 0)
	item = models.ForeignKey(Item)
	desconto = models.DecimalField(verbose_name = 'Desconto', max_digits = 15, decimal_places = 2, default = 0)
	valor_pago = models.DecimalField(verbose_name = 'Valor Pago', max_digits = 15, decimal_places = 2, default = 0)

	#pega chave