from django.shortcuts import render
from meyer.models import *

# Create your views here.
def home(request):
    topics = Topic.objects.all().order_by('order')
#    subtopics = Topic.objects.all().order_by('order')
    for topic in topics:
        topic.subtopics.all().order_by('order')
    return render(request, 'home.html', {'topics':topics, 'a':[1,2,3,4,5]})

#def compare(request):
#    return render(request, "home.back.html", {})
