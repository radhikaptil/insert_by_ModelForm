from django.shortcuts import render

# Create your views here.
from app.forms import TopicForm,WebpageForm

from django.http import HttpResponse

def insert_topic(request):
    TEFO=TopicForm()
    d={'TEFO':TEFO}

    if request.method=='POST':
        TDFO=TopicForm(request.POST)
        if TDFO.is_valid():
            TDFO.save()
            return HttpResponse('Data is inserted succssfully in topic model')
        
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    WEFO=WebpageForm()
    d={'WEFO':WEFO}

    if request.method=='POST':
        WDFO=WebpageForm(request.POST)
        if WDFO.is_valid():
            WDFO.save()
            return HttpResponse('Data in inserted successfully in webpage model')

    return render(request,'insert_webpage.html',d)



