from django.shortcuts import render
from .models import Course
# Create your views here.

def index(request):
    return render(request, 'index.html')

def course_list(request):
    courses = Course.objects.select_related('owner', 'subject').all()
    return render(request, 'course.html', {'courses': courses})
