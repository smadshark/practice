from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import User


# Create your views here.

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        user_pw = request.POST.get('user-pw', '')
        check_pw = request.POST.get('check-pw', '')

        res_data = {}
        if not ( username and user_pw and check_pw ):
            res_data['error'] = '모든 값을 입력해야합니다.'
        elif user_pw != check_pw:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            user = User(
                username=username,
                user_pw=make_password(user_pw)
            )

            user.save()

        return render(request, 'register.html', res_data)
