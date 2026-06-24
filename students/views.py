from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg, Max

from .models import Student, Grade
from .forms import StudentForm, GradeForm


def home(request):

    total_students = Student.objects.count()
    total_grades = Grade.objects.count()

    context = {
        'total_students': total_students,
        'total_grades': total_grades,
    }

    return render(request, 'students/home.html', context)


def student_list(request):

    students = Student.objects.all()

    return render(
        request,
        'students/student_list.html',
        {'students': students}
    )


def student_detail(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    return render(
        request,
        'students/student_detail.html',
        {'student': student}
    )


def add_student(request):

    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('student_list')

    return render(
        request,
        'students/add_student.html',
        {'form': form}
    )


def edit_student(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    form = StudentForm(
        request.POST or None,
        instance=student
    )

    if form.is_valid():
        form.save()
        return redirect('student_list')

    return render(
        request,
        'students/edit_student.html',
        {'form': form}
    )


def delete_student(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(
        request,
        'students/confirm_delete.html',
        {'object': student}
    )


def add_grade(request):

    form = GradeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('student_list')

    return render(
        request,
        'students/add_grade.html',
        {'form': form}
    )


def edit_grade(request, grade_id):

    grade = get_object_or_404(Grade, id=grade_id)

    form = GradeForm(
        request.POST or None,
        instance=grade
    )

    if form.is_valid():
        form.save()
        return redirect(
            'student_detail',
            student_id=grade.student.id
        )

    return render(
        request,
        'students/edit_grade.html',
        {'form': form}
    )


def delete_grade(request, grade_id):

    grade = get_object_or_404(Grade, id=grade_id)

    student_id = grade.student.id

    if request.method == 'POST':
        grade.delete()
        return redirect(
            'student_detail',
            student_id=student_id
        )

    return render(
        request,
        'students/confirm_delete.html',
        {'object': grade}
    )


def topper(request):

    grades = Grade.objects.order_by('-score')

    top_grade = grades.first()

    return render(
        request,
        'students/topper.html',
        {'top_grade': top_grade}
    )


def class_average(request):

    averages = (
        Grade.objects
        .values('subject')
        .annotate(avg_score=Avg('score'))
    )

    return render(
        request,
        'students/class_average.html',
        {'averages': averages}
    )