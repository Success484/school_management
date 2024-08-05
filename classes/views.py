# views.py
from django.shortcuts import render, redirect
from .forms import ClassForm, SubjectForm
from .models import Class, Subject

def create_class(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_list')  # Redirect to the list of classes after saving
    else:
        form = ClassForm()
    return render(request, 'class/create_class.html', {'form': form})


def class_list(request):
    classes = Class.objects.all()
    return render(request, 'class/class_list.html', {'classes': classes})


def create_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')  # Redirect to the list of subjects after saving
    else:
        form = SubjectForm()
    return render(request, 'class/create_subject.html', {'form': form})


def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'class/subject_list.html', {'subjects': subjects})
