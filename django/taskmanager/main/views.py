from django.shortcuts import render, redirect
from .models import Sushi
from .forms import SushiForm


def index(reguest):
    # получить все обьекты
    sushi = Sushi.objects.order_by('-id')
    return render(reguest, 'main/index.html', {'title': 'it_MAX ツ Главная страница', 'sushi': sushi})


def max(reguest):
    return render(reguest, 'main/max.html')


def create(reguest):
    error = ''
    if reguest.method =='POST':
        form = SushiForm(reguest.POST)
        if form.is_valid():
            form.save()
            redirect('home')
            return redirect('home')
        else:
            error = 'Форма была не верной'



    form = SushiForm()
    context = {
        'form': form,
        'error': error
    }
    return render(reguest, 'main/create.html', context)