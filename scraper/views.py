from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from bs4 import BeautifulSoup
from .models import Link
# Create your views here.


def scrape(request):

    if request.method == 'POST':
        url = request.POST.get('url','')
        print('URL ',url)
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'html.parser')

        for link in soup.find_all('a'):
            link_add = (link.get('href'))
            link_name = link.string
            Link.objects.create(address=link_add,name=link_name)
        return HttpResponseRedirect("/")
    else:
        data = Link.objects.all()
        return render(request,'index.html',{'object':data})


def delete(request):
    Link.objects.all().delete()
    return HttpResponseRedirect("/")
