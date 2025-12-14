from django.shortcuts import render, get_object_or_404
from .models import Course
# Create your views here.

# from django.shortcuts import render, get_object_or_404
# from django.views.generic import ListView, TemplateView, DetailView
# from .models import Course

# class CourseListView(ListView):
#     model = Course
#     template_name = 'course.html'
#     context_object_name = 'courses'

# class IndexView(TemplateView):
#     template_name = 'index.html'

# class CourseDetailView(DetailView):
#     model = Course
#     template_name = 'detail.html'
#     context_object_name = 'course'



def index(request):
    return render(request, 'index.html')

def course_list(request):
    courses = Course.objects.select_related('owner', 'subject').all()
    return render(request, 'course.html', {'courses': courses})
    

def course_detail(request, pk):
    course =  get_object_or_404(Course, pk = pk)
    return render(request, 'detail.html', {'course': course})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

