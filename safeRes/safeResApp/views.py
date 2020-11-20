from django.shortcuts import render
from django.views import View

# Create your views here.

def safeMaps(request):
    #가장 먼저 사용자의 요청에 따라 메인 페이지 호?
    return render(request, 'index.html',{})
