from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer

def platform_view(request):
    return render(request, 'task1/platform.html')

from .models import Game

def games_view(request):
    games = Game.objects.all()
    return render(request, 'task1/games.html', {'games': games})



def cart_view(request):
    return render(request, 'task1/cart.html')

users = ['user1', 'user2', 'admin']


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            info['message'] = f'Приветствуем, {username}!'
            users.append(username)
            return render(request, 'task1/registration_page.html', info)

    return render(request, 'task1/registration_page.html', info)


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if Buyer.objects.filter(name=username).exists():
            info['error'] = 'Пользователь уже существует'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        else:

            Buyer.objects.create(name=username, age=age, balance=0.00)
            info['message'] = f'Приветствуем, {username}!'

    return render(request, 'task1/registration_page.html', info)








