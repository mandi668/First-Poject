from django.shortcuts import redirect, render
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.
def home(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(items, 6) 
    page_number = request.GET.get('page')
    try:
        items_paginated = paginator.page(page_number)
    except PageNotAnInteger:
        
        items_paginated = paginator.page(1)
    except EmptyPage:
       
        items_paginated = paginator.page(paginator.num_pages)
    
    context = {"items_value": items_paginated ,  "cat": categories}
    return render(request, "home.html", context)

def about(request):
    staffs = Staff.objects.all()
    categories = Category.objects.all()
    context = {"staff_data": staffs, "cat": categories}
    return render(request, "about.html", context)

def contact(request):
    categories = Category.objects.all()
    context = {"cat": categories}
    if request.method == "POST":
        name = request.POST["name_contact"]
        surname = request.POST["surname_contact"]
        email = request.POST["email_contact"]
        comment = request.POST["comment_contact"]

        Contact(
            contact_name=name,
            contact_surname=surname,
            contact_email=email,
            contact_comment=comment,
        ).save()
        return redirect("/")

    return render(request, "contact.html", context)


def detailItem(request, id):
    categories = Category.objects.all()
    itemdetails = Item.objects.get(item_id=id)
    context = {"details": itemdetails, "cat": categories}
    return render(request, "detailItem.html", context)


def category(request, id):
    categories = Category.objects.all()
    category = Category.objects.get(category_id=id)
    categoryItems = Item.objects.filter(item_category=category)
    context = {"category": category, "cat": categories, "categoryItems": categoryItems}
    return render(request, "categoryPage.html", context)

def your_view(request):
    items_value = YourModel.objects.all() 
    
    paginator = Paginator(items_value, 6)  
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number)  
    
    return render(request, 'home.html', {'page_obj': page_obj})


def reserve(request):
    categories = Category.objects.all()
    context = {"cat": categories}
    if request.method == "POST":
        name = request.POST["name_reserve"]
        surname = request.POST["surname_reserve"]
        email = request.POST["email_reserve"]
        number = request.POST["number_reserve"]
        comment = request.POST["comment_reserve"]

        Reserve(
            reserve_name=name,
            reserve_surname=surname,
            reserve_email=email,
            reserve_number=number,
            reserve_comment=comment,
        ).save()
        return redirect("/")

    return render(request, "reserve.html", context)