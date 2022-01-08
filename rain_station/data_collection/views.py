from django.shortcuts import render
from datetime import datetime
# Create your views here.
from django.http import HttpResponse
def hello_world(request):
     return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
    })