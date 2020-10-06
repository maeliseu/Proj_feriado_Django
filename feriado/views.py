from django.shortcuts import render


def natal(request):
    contexto = {'natal': False,
    'carnaval': False}
    return render(request, 'natal.html', contexto)

def carnaval(request):
    contexto = {'natal': False,
    'carnaval': False}
    return render(request, 'carnaval.html', contexto)

def tiradentes(request):
    contexto = {'natal': False,
    'tiradentes': False}
    return render(request, 'tiradentes.html', contexto)