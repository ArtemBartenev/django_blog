from django.shortcuts import render
from django.http import HttpResponse

def posts_list(request):
    list = ['bottle', 'fork', 'spoon', 'plate', 'candle']
    return render(request, 'first_blog/index.html', context={'list': list})