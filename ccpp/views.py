from django.shortcuts import render, get_object_or_404
from ccpp.models import News

#from django.http import HttpResponse
# Create your views here.

#def show(request):
#    return HttpResponse("Hello Django")

def news_list(request):
    news = News.objects.all()
    return render(request, "ccpp/news_list.html", {"news": news})

def new_single(request, pk):
    new = get_object_or_404(News, id=pk)
    return render(request, "ccpp/new_single.html", {"new": new})