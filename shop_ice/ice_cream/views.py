from django.shortcuts import render
from ice_cream.models import IceCream
from django.shortcuts import get_object_or_404


def ice_cream_detail(request, pk):
    ice_cream = get_object_or_404(
        IceCream.objects.filter(is_published = True, category__is_published = True),
        pk=pk
    )
    context = {
        'ice_cream' : ice_cream
    }
    return render(request, 'ice_cream/detail.html', context)


def ice_cream_list(request):
    ice_cream_list = IceCream.objects.select_related('category').filter(
        is_published = True,
        category__is_published = True
    ).order_by ('category')
    context = {
        'ice_cream_list' : ice_cream_list
    }
    return render(request, 'ice_cream/list.html', context)
