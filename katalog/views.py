from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'list_katalog': data_barang_katalog,
        'nama': 'Alifio Fathan Haryanto',
        'npm': 2106653483,
        
    
}
    return render(request, "katalog.html", context)
