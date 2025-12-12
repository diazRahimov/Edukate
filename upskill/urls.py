from django.urls import path
from .views import index, course_list


urlpatterns = [
    path('',index, name='index'),
    path('courses/', course_list, name='course_list')
]
