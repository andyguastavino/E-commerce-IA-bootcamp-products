
from django.shortcuts import render, redirect, get_object_or_404
from .models import Section, Category, Subcategory, Product
from .forms import ProductForm, CategoryForm, SubcategoryForm, SectionForm
from django.contrib import messages
from django.core.paginator import Paginator #Importando paginator para manejar la paginacion de products


#Manejo de Productos

def product_list(request):
    # Obteniendo todos los productos
    products = Product.objects.all()

    # Filtros opcionales
    section_id = request.GET.get('section')
    category_id = request.GET.get('category')
    subcategory_id = request.GET.get('subcategory')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    # Aplicar filtros si están presentes
    if section_id:
        products = products.filter(section_id=section_id)
    if category_id:
        products = products.filter(category_id=category_id)
    if subcategory_id:
        products = products.filter(subcategories__id=subcategory_id)
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    # Paginación
    paginator = Paginator(products, 5)  # Muestra 5 productos por página
    page_number = request.GET.get('page')  # Obtén el número de página de la solicitud
    page_obj = paginator.get_page(page_number)  # Obtén los objetos de la página

    # Obtener las secciones, categorías y subcategorías para los filtros
    sections = Section.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()

    # Pasar los filtros seleccionados al contexto para mantener el estado en el formulario
    context = {
        'page_obj': page_obj,
        'sections': sections,
        'categories': categories,
        'subcategories': subcategories,
        'selected_section': section_id,
        'selected_category': category_id,
        'selected_subcategory': subcategory_id,
        'min_price': min_price,
        'max_price': max_price,
    }

    return render(request, 'products/product_list.html', context)
    

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})

def product_edit(request,pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        messages.success(request, 'El producto ha sido eliminado con éxito.')
        return redirect('product_list')

    return render(request, 'products/product_confirm_delete.html', {'product': product})


#Manejo de categorias

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'products/category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'products/category_form.html', {'form': form})

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'products/category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('category_list')


#Manejo de Subcategorias
def subcategory_list(request):
    subcategories = Subcategory.objects.all()
    return render(request, 'products/subcategory_list.html', {'subcategories': subcategories})
def subcategory_create(request):
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subcategory_list')
    else:
        form = SubcategoryForm()
    return render(request, 'products/subcategory_form.html', {'form': form})

def subcategory_edit(request, pk):
    subcategory = get_object_or_404(Subcategory, pk=pk)
    if request.method == 'POST':
        form = SubcategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('subcategory_list')
    else:
        form = SubcategoryForm(instance=subcategory)
    return render(request, 'products/subcategory_form.html', {'form': form})

def subcategory_delete(request, pk):
    subcategory = get_object_or_404(Subcategory, pk=pk)
    subcategory.delete()
    return redirect('subcategory_list')



#Manejo de Secciones

def section_list(request):
    sections = Section.objects.all()
    return render(request, 'products/section_list.html', {'sections': sections})

def section_create(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('section_list')
    else:
        form = SectionForm()
    return render(request, 'products/section_form.html', {'form': form})

def section_edit(request, pk):
    section = get_object_or_404(Section, pk=pk)
    if request.method == 'POST':
        form = SectionForm(request.POST, instance=section)
        if form.is_valid():
            form.save()
            return redirect('section_list')
    else:
        form = SectionForm(instance=section)
    return render(request, 'products/section_form.html', {'form': form})

def section_delete(request, pk):
    section = get_object_or_404(Section, pk=pk)
    section.delete()
    return redirect('section_list')


