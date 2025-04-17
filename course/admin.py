from django.contrib import admin
# from django.contrib.auth.models import Group
from course.models import Subjects, Course, Student, Teacher


# Register your models here.

# admin.site.register(Subjects)
# admin.site.register(Course)
# admin.site.register(Teacher)
# admin.site.register(Group)
# admin.site.register(Student)
# admin.site.register(Enrollment)
# admin.site.unregister(Group)

@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at', 'updated_at')
    search_fields = ('title',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description', 'duration', 'price')
    search_fields = ('title', 'description')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name', 'email','works_as', 'teacher_image')
    search_fields = ('first_name', 'last_name', 'email')



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','student_id_number', 'first_name','last_name', 'email')
    search_fields = ('first_name', 'email')

