from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Product, CATEGORY_CHOICES
from webapp.forms import ProductForm
from django.http import HttpResponseNotAllowed


def index_view(request):
    data = Product.objects.all()
    return render(request, 'index.html', context={
        'products': data
    })


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, "product.html", context)


def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'product_delete.html', context={'product': product})
    elif request.method == 'POST':
        product.delete()
        return redirect("index")


def product_create_view(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, 'product_create.html', context={
            'form': ProductForm()
        })
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            category = form.cleaned_data['category']
            amount = form.cleaned_data['amount']
            price = form.cleaned_data['price']
            product = Product.objects.create(name=name, description=description,
                                             category=category, amount=amount, price=price)
            return redirect('product_view', pk=product.pk)
        else:
            return render(request, 'product_create.html', context={'form': form})
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
#
#
# def task_update_view(request, pk):
#     task = get_object_or_404(To_Do_list, pk=pk)
#     if request.method == "GET":
#         form = TaskForm(data={
#             'status': task.status,
#             'summary': task.summary,
#             'description': task.description,
#             'completion_time': task.completion_time
#         })
#         return render(request, 'task_update.html', context={'form': form, 'task': task})
#     elif request.method == 'POST':
#         form = TaskForm(data=request.POST)
#         if form.is_valid():
#             task.status = form.cleaned_data['status']
#             task.summary = form.cleaned_data['summary']
#             task.description = form.cleaned_data['description']
#             task.completion_time = form.cleaned_data['completion_time']
#             task.save()
#             return redirect('task_view', pk=task.pk)
#         else:
#             return render(request, 'task_update.html', context={'task': task, 'form': form})
#     else:
#         return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
#
#
#
