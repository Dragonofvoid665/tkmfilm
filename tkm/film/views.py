from django.shortcuts import render
from django.http import HttpRequest, HttpResponse,HttpResponseRedirect
from film.models import Product, Company


def ActorsVeiw(request):
    products = Company.objets.all()
    return render(request,'test.html',{products:"products"})