# student/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

def student_panel(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            form = StudentForm()  # Clear the form after saving

    students = Student.objects.all()
    return render(request, 'student/panel.html', {'form': form, 'students': students})

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_panel')
    else:
        form = StudentForm(instance=student)
    students = Student.objects.all()
    return render(request, 'student/panel.html', {'students': students, 'form': form, 'edit_id': id})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_panel')