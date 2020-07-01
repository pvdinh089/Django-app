from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,'layout/main.html')
    #return HttpResponse('Đây là chương trình đầu tiên')