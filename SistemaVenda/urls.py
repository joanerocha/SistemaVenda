"""SistemaVenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$','joane.views.index'),
    url(r'^cliente/$','joane.views.cliente', name='cliente_visual'),
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': './media/'}),
    url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': './static/',}),
    url(r'^editarcliente/(?P<id_cliente>\d+)', 'joane.views.editarcliente',name='editar_cliente'),
    url(r'^incluircliente/', 'joane.views.incluircliente',name='incluir_cliente'),
    url(r'^fotocliente/(?P<id_cliente>\d+)', 'joane.views.fotocliente',name='foto_cliente'),
    url(r'^excluircliente/(?P<id_cliente>\d+)', 'joane.views.excluircliente',name='excluir_cliente'),
    url(r'^entrar/','joane.views.entrar',name='entrar'),
    url(r'^fornecedor/$','joane.views.fornecedor', name='fornecedor_visual'),
    url(r'^editarfornecedor/(?P<id_fornecedor>\d+)', 'joane.views.editarfornecedor',name='editar_fornecedor'),
    url(r'^incluirfornecedor/', 'joane.views.incluirfornecedor',name='incluir_fornecedor'),
    url(r'^fotofornecedor/(?P<id_fornecedor>\d+)', 'joane.views.fotofornecedor',name='foto_fornecedor'),
    url(r'^excluirfornecedor/(?P<id_fornecedor>\d+)', 'joane.views.excluirfornecedor',name='excluir_fornecedor'),
    url(r'^produto/$','joane.views.produto', name='produto_visual'),
    url(r'^editarproduto/(?P<id_produto>\d+)', 'joane.views.editarproduto',name='editar_produto'),
    url(r'^incluirproduto/', 'joane.views.incluirproduto',name='incluir_produto'),
    url(r'^fotoproduto/(?P<id_produto>\d+)', 'joane.views.fotoproduto',name='foto_produto'),
    url(r'^excluirproduto/(?P<id_produto>\d+)', 'joane.views.excluirproduto',name='excluir_produto'),
]
