from django.shortcuts import render, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Product
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'catalog/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()


def product_page(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        description_parts = product.description.split(';')
    except Product.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'catalog/product_page.html', {
        'product': product,
        'description_parts': description_parts,
    })


def search(request):
    search_word = request.GET['text']
    if search_word:
        products = Product.objects.filter(
            title__contains = search_word
        )
        context = {'products': products}
        return render(request, 'catalog/index.html', context)
    else:
        return HttpResponseRedirect(reverse('catalog:catalog'))