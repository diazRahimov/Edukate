# from django.conf import settings
# from django.urls import path
# from django.conf.urls.static import static
# from .views import CourseListView, IndexView, CourseDetailView


# urlpatterns = [
#     path('', IndexView.as_view(), name='index'),
#     path('courses/', CourseListView.as_view(), name='course_list'),
#     path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import CourseListView, IndexView, CourseDetailView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/subject/<int:subject_id>/', CourseListView.as_view(), name = 'courses_by_subject'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('logout/', LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)