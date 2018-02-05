"""
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    """
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo, Category, Description
from django.shortcuts import get_object_or_404, render



def index(request):
    latest_category_list = Category.objects.order_by('-pub_date')[:5]
    context = {
        'latest_category_list': latest_category_list,
    }
    return render(request, 'todolist/index.html', context)


def detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'todolist/detail.html', {'category': category})

def dsc(request, category_id):
    description_text = get_object_or_404(Category, pk=category_id)
    context = {
        'description_text': description_text,
    }
    return render(request, 'todolist/dsc.html', context)


"""

def description(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    selected_description = category.tudo_set.get(pk=request.POST['todo'])
    return HttpResponseRedirect(reverse('todolist:results', args=(category.id,)))


"""





#def results(request, category_id):
  #  response = "%s kategorideki yapacakar listenize bakıyorsunuz."
   # return HttpResponse(response % category_id)


"""def tudos(request, id):
    todo = Todo.objects.get(id=id)

    context = {
        'todo':todo
    }
    return render(request, 'dsc.html', context)
    
"""
