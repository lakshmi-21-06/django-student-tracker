from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)

    def average_grade(self):
        grades = self.grades.all()

        if grades.exists():
            total = sum(grade.score for grade in grades)
            return round(total / grades.count(), 2)

        return 0

    def __str__(self):
        return self.name


class Grade(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='grades'
    )

    subject = models.CharField(max_length=50)

    score = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )

    def __str__(self):
        return f"{self.student.name} - {self.subject}"