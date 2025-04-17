from django.urls import path
from course import views
from course.views import CourseDetailView, TeacherListView, TeacherDetailView, CourseListView, SubjectDetailView

app_name = 'course'
urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='index'),
    path('subject/<pk>/', SubjectDetailView.as_view(), name='subject-detail'),
    path('courses/', CourseListView.as_view(), name='course_list_view'),
    path('course/<course_id>/', views.index, name='course_list'),
    path('course_detail/<pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('teachers/', TeacherListView.as_view(), name='teachers_list'),
    path('teacher/<pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('blog/', views.blog_show_view, name='blog'),
]