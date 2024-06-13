from django.shortcuts import render
from .models import Shop

def index(request):
    shops = Shop.objects.filter(
        (Q(category__icontains='Fluorescence') |
         Q(category__icontains='Carat') |
         Q(category__icontains='Color Grade') |
         Q(category__icontains='Cutting Style') |
         Q(name__icontains='FLUORESCENCE') |
         Q(category__icontains='Round Brilliant') |
         Q(subcategory__icontains='CUT PROPORTION') |
         Q(subcategory__icontains='CUT GRADE') |
         Q(subcategory__icontains='POLISH') |
         Q(subcategory__icontains='SYMMETRY') |
         Q(subcategory__icontains='THIN-MEDIUM') |
         Q(subcategory__icontains='MEDIUM WHITISH BLUE')) &
        (Q(price__gte=0) & Q(price__lte=4.41))
    )
    return render(request, 'shop/index.html', {'shops': shops})