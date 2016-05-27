# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Documento)
admin.site.register(Endereco)
admin.site.register(Email)
admin.site.register(Fornecedor)
admin.site.register(FDocumento)
admin.site.register(FEndereco)
admin.site.register(FEmail)
admin.site.register(Unidade)
admin.site.register(Produto)
admin.site.register(Item)
admin.site.register(Pedido)
admin.site.register(Venda)
admin.site.register(Financeiro)
#admin.site.register(LancamentoCliente)