from django.shortcuts import render, get_object_or_404
from .models import Phone
def catalogue(request):
    sort_by = request.GET.get("sort", "name")
    if sort_by == "min_price":
        phones = Phone.objects.all().order_by("price")
    elif sort_by == "max_price":
        phones = Phone.objects.all().order_by("-price")
    else:
        phones = Phone.objects.all().order_by("name")
    return render(request, "catalogue.html", {"phones": phones})

def phone_detail(request, slug):
    phone = get_object_or_404(Phone, slug = slug)
    return render(request, "phone_detail.html", {"phone": phone} )



