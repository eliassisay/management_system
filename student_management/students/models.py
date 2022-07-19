
from django.db import models

class Students(models.Model):
    student_number=models.PositiveBigIntegerField()
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    field_if_study=models.CharField(max_length=50)
    gpa=models.FloatField()
    def __str__(self):
        return f'Students: {self.first_name} {self.last_name}'
