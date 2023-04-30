import sqlite3
from itertools import chain

import pandas as pd
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, request
from django.shortcuts import render
from django.views.generic import ListView

from main_page.models import Gost, Category, Ansi, Api, Asme, Astm, Bs, Din, Dd, Dvs, En, Iec, Vdi, Pd, Iso


# Create your views here.

def index(request):
    categories = Category.objects.all()
    return render(request, 'main_page/home.html', {'categories': categories})


def view_all_document(request):
    documents = Gost.objects.all()
    paginator = Paginator(documents, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main_page/view_all_document.html', {'page_obj': page_obj})


def populating_the_database(request):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    df = pd.read_excel('gost.xlsx')
    df.to_sql('main_page_gost', conn, if_exists='replace', index=True)
    c.execute('''
    SELECT * FROM main_page_gost''')
    return HttpResponse(f'{df}')


class SearchView(ListView):
    model = Gost
    template_name = 'main_page/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')

        object_list = list(chain(Gost.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)),
                                 Iso.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)),
                                 Ansi.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)),
                                 Api.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)),
                                 Asme.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)),
                                 Astm.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)),
                                 Bs.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)),
                                 Din.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)),
                                 Dd.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)),
                                 Dvs.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)),
                                 En.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)),
                                 Iec.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)),
                                 Vdi.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)),
                                 Pd.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))))
        return object_list


def right_holders(request):
    return render(request, 'main_page/right_holders.html')


def how_to_get(request):
    return render(request, 'main_page/how_to_get.html')


def how_to_order(request):
    return render(request, 'main_page/how_to_order.html')


def about_cat(request, cat):
    if cat == 'gost':
        documents = Gost.objects.all()
        paginator = Paginator(documents, 100)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'main_page/category.html', {'page_obj': page_obj})
    elif cat == 'iso':
        documents = Iso.objects.all()
        return render(request, 'main_page/category.html', {'documents': documents})
    elif cat == 'ansi':
        documents = Ansi.objects.all()
        return render(request, 'main_page/category.html', {'documents': documents})
    elif cat == 'api':
        documents = Api.objects.all()
        return render(request, 'main_page/category.html', {'documents': documents})
    elif cat == 'asme':
        documents = Asme.objects.all()
        return render(request, 'main_page/category.html', {'documents': documents})
    elif cat == 'astm':
        documents = Astm.objects.all()
        return render(request, 'main_page/category.html', {'documents': documents})
    elif cat == 'bs':
        documents = Bs.objects.all()
        return render(request, 'main_page/category.html', {'documents': documents})
    elif cat == 'din':
        documents = Din.objects.all()
        return render(request, 'main_page/category.html', {'documents': documents})
    elif cat == 'dd':
        documents = Dd.objects.all()
        return render(request, 'main_page/category.html', {'documents': documents})
    elif cat == 'dvs':
        documents = Dvs.objects.all()
        return render(request, 'main_page/category.html', {'documents': documents})
    elif cat == 'en':
        documents = En.objects.all()
        return render(request, 'main_page/category.html', {'documents': documents})
    elif cat == 'iec':
        documents = Iec.objects.all()
        return render(request, 'main_page/category.html', {'documents': documents})
    elif cat == 'vdi':
        documents = Vdi.objects.all()
        return render(request, 'main_page/category.html', {'documents': documents})
    elif cat == 'pd':
        documents = Pd.objects.all()
        return render(request, 'main_page/category.html', {'documents': documents})


def about_doc(request, cat, doc):
    if cat == 'gost':
        categories = Gost.objects.filter(id=doc)
        return render(request, 'main_page/view_one_document.html', {'categories': categories})
    elif cat == 'iso':
        categories = Iso.objects.filter(id=doc)
        return render(request, 'main_page/view_one_document.html', {'categories': categories})
    elif cat == 'ansi':
        categories = Ansi.objects.filter(id=doc)
        return render(request, 'main_page/view_one_document.html', {'categories': categories})
    elif cat == 'api':
        categories = Api.objects.filter(id=doc)
        return render(request, 'main_page/view_one_document.html', {'categories': categories})
    elif cat == 'asme':
        categories = Asme.objects.filter(id=doc)
        return render(request, 'main_page/view_one_document.html', {'categories': categories})
    elif cat == 'astm':
        categories = Astm.objects.filter(id=doc)
        return render(request, 'main_page/view_one_document.html', {'categories': categories})
    elif cat == 'bs':
        categories = Bs.objects.filter(id=doc)
        return render(request, 'main_page/view_one_document.html', {'categories': categories})
    elif cat == 'din':
        categories = Din.objects.filter(id=doc)
        return render(request, 'main_page/view_one_document.html', {'categories': categories})
    elif cat == 'dd':
        categories = Dd.objects.filter(id=doc)
        return render(request, 'main_page/view_one_document.html', {'categories': categories})
    elif cat == 'dvs':
        categories = Dvs.objects.filter(id=doc)
        return render(request, 'main_page/view_one_document.html', {'categories': categories})
    elif cat == 'en':
        categories = En.objects.filter(id=doc)
        return render(request, 'main_page/view_one_document.html', {'categories': categories})
    elif cat == 'iec':
        categories = Iec.objects.filter(id=doc)
        return render(request, 'main_page/view_one_document.html', {'categories': categories})
    elif cat == 'vdi':
        categories = Vdi.objects.filter(id=doc)
        return render(request, 'main_page/view_one_document.html', {'categories': categories})
    elif cat == 'pd':
        categories = Pd.objects.filter(id=doc)
        return render(request, 'main_page/view_one_document.html', {'categories': categories})
    # categories = Gost.objects.filter(id=doc)
    # return render(request, 'main_page/view_one_document.html', {'categories': categories})
