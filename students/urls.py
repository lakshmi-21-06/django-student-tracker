from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('students/', views.student_list, name='student_list'),

    path('add-student/', views.add_student, name='add_student'),
    path('edit-student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),

    path('add-grade/', views.add_grade, name='add_grade'),
    path('edit-grade/<int:grade_id>/', views.edit_grade, name='edit_grade'),
    path('delete-grade/<int:grade_id>/', views.delete_grade, name='delete_grade'),

    path('student/<int:student_id>/', views.student_detail, name='student_detail'),

    path('topper/', views.topper, name='topper'),
    path('class-average/', views.class_average, name='class_average'),
]