import random
import string
from django.db import models
# from urllib.parse import urlparse, parse_qs
# from decimal import Decimal
# Create your models here.

class Subjects(models.Model): #Category
    """This model works as category for each course"""
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True) #when added to there
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Subjects"

    def __str__(self):
        return self.title


class SubjectVideo(models.Model):
    """This model is for storing videos to subject model"""
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=255, blank=True, null=True)
    video_file = models.FileField(upload_to='subject_videos/')  # Store uploaded video files
    order = models.IntegerField(default=1)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title if self.title else str(self.video_file)


class Course(models.Model):
    """This model works as courses for each subject and also makes student connected to course too."""
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=14, decimal_places=0)
    student_study = models.IntegerField(null=True, blank=True)
    lesson_hours = models.IntegerField(null=True, blank=True)
    duration = models.PositiveIntegerField()
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='course', null=True,blank=True)
    rating = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"Title - {self.title}, price - {self.price}"

    class Meta:
        verbose_name_plural = "Courses"


class Teacher(models.Model):
    """This model is for teachers. teacher will have group"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True,max_length=100, null=True, blank=True)
    works_as = models.CharField(max_length=100, null=True, blank=True)
    salary = models.DecimalField(max_digits=14, decimal_places=0, default=0)
    teacher_image = models.ImageField(null=True, blank=True)
    class Meta:
        verbose_name_plural = "Teachers"

    def __str__(self):
        return self.first_name + " " + self.last_name


class Group(models.Model):
    """This is group model. it will be depended on Teacher and Course"""
    group_name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    end_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    schedule = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Groups"

    def __str__(self):
        return f"Group name - {self.group_name}        teacher - {self.teacher}"

def generate_student_id():
    """5 digits student id generator"""
    while True:
        student_id = ''.join(random.choices(string.digits, k=5))
        if not Student.objects.filter(student_id_number=student_id).exists():
            return student_id

class Student(models.Model):
    """This is student model. It is made for registering student and connecting him/her to course"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id_number = models.CharField(max_length=100, null=True, blank=True, default=generate_student_id, editable=False)
    image = models.ImageField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    # Add other relevant fields for your student model

    def __str__(self):
        return f"ID: {self.student_id_number} full name: {self.first_name} {self.last_name} "

    class Meta:
        verbose_name_plural = "Students"


class Enrollment(models.Model):
    """This model is for students to put them in groups"""
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    grade = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Enrollments"
        unique_together = ('student', 'group') #student cannot participate in the same group twice

    def __str__(self):
        return f"Enrollment - {self.student} - {self.enrollment_date}"


class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=255, blank=True, null=True)
    video_file = models.FileField(upload_to='course_videos/')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='videos', null=True, blank=True)
    order = models.IntegerField(default=1)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title if self.title else str(self.video_file)