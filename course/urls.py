from django.urls import path
from course import views
from course.views import CourseDetailView, TeacherListView, TeacherDetailView, CourseBaseListView, AboutView, \
    CourseShowListView, CourseDetailShowView

app_name = 'course'
urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='index'),
    path('courses/', CourseBaseListView.as_view(), name='course_list_view'),
    # path('course/<course_id>/', views.index, name='course_list'),
    path('course_detail/<pk>/', CourseDetailView.as_view(), name='course_detail'),


    path('course_by_subject/<int:subject_id>/', CourseShowListView.as_view(), name='course_by_subject'), #working
    path('course_detail/<int:pk>/', CourseDetailShowView.as_view(), name='course_detail_id'),



    path('teachers/', TeacherListView.as_view(), name='teachers_list'),
    path('teacher/<pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('about/', AboutView.as_view(), name='about_view'),
    path('show_course_detail/', views.course_detail_show, name='course_detail_show'),
]