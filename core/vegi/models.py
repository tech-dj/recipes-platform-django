from django.db import models
from django.contrib.auth.models import User  # Correct import




# Receipe Model
class Receipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    Receipe_name = models.CharField(max_length=50)
    Receipe_description = models.TextField()
    Receipe_image = models.ImageField(upload_to='receipe_images')
    Receipe_view_count = models.IntegerField(default=1)

class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department

    class Meta:
        ordering = ['department']

# StudentID Model
class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id

# Student Model
class Student(models.Model):  # Added missing inheritance
    department = models.ForeignKey(Department, related_name="depart", on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentID, related_name="studentid", on_delete=models.CASCADE)  # Fixed on_delete
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)  # Fixed spelling
    student_age = models.IntegerField(default=18)
    student_address = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name

    class Meta:
        ordering = ['student_name']
        verbose_name = "student"  # Fixed incorrect tuple format

