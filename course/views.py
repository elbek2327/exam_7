
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.views import View
from course.models import Subjects, Course, Teacher, Group, Video, SubjectVideo


# Create your views here.

def index(request, course_id:int|None=None):
    """Index view. Default template"""
    subjects = Subjects.objects.all()
    courses_all_query = Course.objects.all()

    if course_id:
        courses = courses_all_query.filter(course_id=course_id)
    else:
        courses = courses_all_query
    teachers = Teacher.objects.all()
    context = {
        'subjects': subjects,
        'courses': courses,
        'teachers': teachers
    }

    return render(request, 'course/index.html', context)


class SubjectDetailView(View):
    model = Subjects
    template_name = 'course/subject_details.html'
    context_object_name = 'subject'




class CourseListView(ListView):
    """This view is for displaying courses list"""
    model = Subjects, Course
    template_name = 'course/course.html'

    def get_queryset(self):
        """subjects for Subject model"""
        return Subjects.objects.all()

    def get_context_data(self, **kwargs):
        """for All models"""
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context


class CourseDetailView(DetailView):
    """This view is for showing details for all courses"""
    template_name = 'course/course_detail.html'
    model = Course
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course=self.get_object()
        teachers = Teacher.objects.filter(group__course=course).distinct()
        videos = Video.objects.filter(course=course).order_by('order')
        context['teachers'] = teachers
        context['groups'] = Group.objects.filter(course=course)
        context['videos'] = videos
        return context


class TeacherListView(ListView):
    """This view is for displaying all teachers"""
    template_name = 'course/teacher.html'
    model = Teacher


class TeacherDetailView(DetailView):
    """This view is for showing details for a teacher"""
    template_name = 'course/teacher_detail.html'
    model = Teacher
    context_object_name = 'teacher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher = self.get_object()
        context['courses_taught'] = Course.objects.filter(group__teacher=teacher).distinct()
        context['groups_instructed'] = Group.objects.filter(teacher=teacher)
        return context







def blog_show_view(request):
    return render(request, 'course/blog.html')