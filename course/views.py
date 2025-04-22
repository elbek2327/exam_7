
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView
from course.models import Subjects, Course, Teacher, CourseVideSave


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


class AboutView(TemplateView):
    """Only for About button"""
    template_name = 'course/about.html'


class CourseBaseListView(ListView):
    """This view is for displaying courses list. Index html button Courses"""
    model = Subjects, Course
    template_name = 'course/course_base.html'

    def get_queryset(self):
        """subjects for Subject model"""
        return Subjects.objects.all()

    def get_context_data(self, **kwargs):
        """for All models"""
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context


class CourseShowListView(ListView):
    """Bu course_list.html uchun courseni subject_id bn olish uchun"""
    model = Course
    template_name = 'course/course_list.html'
    context_object_name = 'courses'

    def get_queryset(self):
        subject_id = self.kwargs.get('subject_id')
        self.subject = get_object_or_404(Subjects, id=subject_id)
        return Course.objects.filter(subject=self.subject)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = self.subject
        context['all_subjects'] = Subjects.objects.all()  # Add all subjects
        return context


class CourseDetailShowView(DetailView):
    """This is for showing all courses when entered by its id"""
    model = Course, CourseVideSave
    template_name = 'course/course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        context['course_videos'] = CourseVideSave.objects.filter(course=course)
        return context



class CourseDetailView(DetailView):
    """This view is for showing details for all courses"""
    template_name = 'course/course_detail.html'
    model = Course
    context_object_name = 'course'
    courses = Course.objects.all


class CourseVideoView(DetailView):
    model = CourseVideSave
    template_name = 'course/course_video.html'
    context_object_name = 'course_video'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course_video'] = self.object
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
        return context

def course_detail_show(request):
    """Just protytipe for course_detail.html"""
    return render(request, 'course/course_detail.html')