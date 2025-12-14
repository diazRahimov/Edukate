from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import course_list, index, course_detail
from . import views 
urlpatterns = [
    path('', index, name='index'),
    path('courses/', course_list, name='course_list'),
    path('courses/<int:pk>/', course_detail, name='course_detail'),
    path('', views.index, name='index'),
    path('courses/', views.course_list, name='course_list'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)