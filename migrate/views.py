from django.shortcuts import render, redirect, get_object_or_404
from .models import Food, WishList
from .forms import FoodSearchForm, WishListForm
from django.core.paginator import Paginator

# 搜索食物並顯示結果
def search_food(request):
    if request.method == 'POST':
        form = FoodSearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            foods = Food.objects.filter(name__icontains=name)
            if not foods.exists():
                return render(request, 'search_results.html', {'error': '暫無此項食物數據', 'form': form, 'wishlist_form': WishListForm(initial={'name': name})})
            return render(request, 'search_results.html', {'foods': foods})
    else:
        form = FoodSearchForm()
    return render(request, 'search_food.html', {'form': form})

# 將食物、數量添加到視窗中

def addfood(request, food_id):
    if food_id == 0:
        return redirect('search_food')
    if request.method == 'POST':
        quantity = request.POST.get('quantity', 0)
        try:
            quantity = float(quantity)

            if quantity <= 0:
                return render(request, 'search_results.html', {
                    'error': "數量必須為正",
                    'foods': Food.objects.filter(pk=food_id)
                })

            food = get_object_or_404(Food, pk=food_id)
            if 'food_list' not in request.session:
                request.session['food_list'] = []
            request.session['food_list'].append({
                'name': food.name,
                'quantity': quantity,
                'unit': food.unit,
                'carbon_footprint': food.carbon_footprint,
                'total_carbon': quantity * food.carbon_footprint
            })
            request.session.modified = True
            return redirect('total_carbon')
        except ValueError:
            return render(request, 'search_results.html', {
                'error': "请输入有效的数量",
                'foods': Food.objects.filter(pk=food_id)
            })
    else:
        return redirect('search_food')

# 清空食物列表
def clear_food_list(request):
    if 'food_list' in request.session:
        del request.session['food_list']
    return redirect('search_food')

def about(request):
    return render(request, 'about.html')

def view_wishlist(request):
    wishlist_items = WishList.objects.all()
    return render(request, 'view_wishlist.html', {'wishlist_items': wishlist_items})

def add_to_wishlist(request):
    if request.method == 'POST':
        form = WishListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_wishlist')
    return redirect('search_food')

# 列出所有已有的食物
def food_list(request):
    foods = Food.objects.all()
    paginator = Paginator(foods, 20)  # 每頁顯示20個項目
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'food_list.html', {'page_obj': page_obj})

# 显示当前总碳足迹
def total_carbon(request):
    food_list = request.session.get('food_list', [])
    total_carbon = sum(item['total_carbon'] for item in food_list)
    exceed_limit = total_carbon > 5
    return render(request, 'total_carbon.html', {
        'food_list': food_list,
        'total_carbon': total_carbon,
        'exceed_limit': exceed_limit
    })
