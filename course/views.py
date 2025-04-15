from django.shortcuts import render

from course.models import Subjects


# Create your views here.

def index(request):
    """Index view. Default template"""
    subjects = Subjects.objects.all()

    context = {
        'subjects': subjects,
    }

    return render(request, 'course/index.html', context)


