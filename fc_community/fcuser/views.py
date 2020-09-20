
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Fcuser
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.


def home(request):
    # home 함수는 session에 id 값이 저장되어 있는 경우에는 로그인된 화면을 보여준다.
    user_id = request.session.get('user')
    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser.username)

    return HttpResponse('home!!')


def login(request):
    # login 함수는 GET, POST 방식으로 구분하여 처리한다.
    # 특히 POST 방식의 경우에는 session 을 이용해 로그인을 처리한다.
    if request.method == 'GET':
        return render(request, 'login.html', res_data)
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data = {}
        if not (username and password):
            res_data['error'] = '모든 값을 입력해주세요'
        else:
            fcuser = Fcuser.objects.get(username=username)
            if check_password(password, fcuser.password):
                # login process done
                request.session['user'] = fcuser.id
                return redirect('/')
                # session !!
                # go to the home !! (redirect)
                pass
            else:
                res_data['error'] = '비밀번호가 틀렸습니다.'
        return render(request, 'login.html', res_data)


def logout(request):
    # logout 을 구현하는 방법은 간단!! session 내부에 존재하는 값을 삭제만 해주면 된다.
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        # response data 의 약어 입니다.
        res_data = {}

        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력해야합니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            fcuser = Fcuser(
                username=username,
                useremail=useremail,
                password=make_password(password)
            )

            fcuser.save()

        return render(request, 'register.html', res_data)
