from django.shortcuts import render
from .models import Job

def home(request):
    #this line grabs all the 'Job' objects in the
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})
