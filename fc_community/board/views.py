from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404
from fcuser.models import Fcuser
from .models import Board
from .forms import BoardForm
# Create your views here.


def board_list(request):
    board = Board.objects.all().order_by('-id')
    return render(request, 'board_list.html', {'boards': boards})
    # if request.method == "GET":
    #     return render(request, 'board_list.html')

    # elif request.method == "POST":
    #     return render(request, 'board_list.html')
