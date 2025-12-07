from django.http import HttpResponse

def index(request):
    return HttpResponse('<h2>Главная</h2>')

def about(request):
    return HttpResponse('<h2>О сайте</h2>')

def contact(request):
    return HttpResponse('<h2>Контакты</h2>')

def products(request, productid):
    output = '<h2>Продукт № {0}</h2>'.format(productid)
    return HttpResponse(output)

def users(request, id, name):
    output = '<h2>Пользователь</h2><h3>id: {0} имя: {1}</h3>'.format(id,name)
    return HttpResponse(output)

def products_category(request, productid):
    category = request.GET.get('cat', '')
    output = '<h2>Product # {0} Category: {1}</h2>'.format(productid, category)
    return HttpResponse(output)

def user(request):
    id = request.GET.get("id", 1)
    name = request.GET.get('name', 'Tom')
    output = '<h2>User</h2><h3>id: {0} name: {1}</h3>'.format(id, name)
    return HttpResponse(output)

