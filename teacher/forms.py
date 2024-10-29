from django import forms
from teacher.models import Attendance, StudentGradeModel, StudentPosition, SchemeOfWork, TeacherClass
import calendar
from classes.models import Subject


class TeacherClassForm(forms.ModelForm):
    class Meta:
        model = TeacherClass
        fields = ['class_name', 'subjects']
        widgets = {
            'class_name': forms.SelectMultiple(attrs={'class': ' select2-multiple class-form'}),
            'subjects': forms.SelectMultiple(attrs={'class': ' select2-multiple class-form'}),
        }

        

class AttendanceMonthForm(forms.Form):
    month = forms.ChoiceField(choices=[(str(i), calendar.month_name[i]) for i in range(1, 13)], widget=forms.Select(attrs={'class': 'final-grade'}))
    year = forms.ChoiceField(choices=[(str(y), y) for y in range(2024, 2034)], widget=forms.Select(attrs={'class': 'final-grade'}))


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['class_info', 'status1', 'status2', 
                  'status3', 'status4', 'status5', 'status6', 'status7', 
                  'status8', 'status9', 'status10', 'status11', 'status12', 
                  'status13', 'status14', 'status15', 'status16', 'status17', 
                  'status18', 'status19', 'status20', 'status21', 'status22',
                  'status23']
        widgets = {
            'status1': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status2': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status3': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status4': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status5': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status6': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status7': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status8': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status9': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status10': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status11': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status12': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status13': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status14': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status15': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status16': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status17': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status18': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status19': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status20': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status21': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status22': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
            'status23': forms.Select(choices=Attendance.STATUS_CHOICES, attrs={'class': 'form-control'}),
        }


class StudentGradeForm(forms.ModelForm):
    year = forms.ChoiceField(
        choices=[(str(y), y) for y in range(2024, 2034)],
        widget=forms.Select(attrs={'class': 'final-grade '})
    )

    class Meta:
        model = StudentGradeModel
        fields = ['subject', 'term', 'year', 'first_test_score', 'second_test_score', 'exam_score', 
                  'out_of', 'first_test_grade', 'second_test_grade', 'exam_grade', 'final_grade']
        widgets = {
            'subject': forms.Select(attrs={'class': 'final-grade'}),
            'first_test_score': forms.TextInput(attrs={'class': 'final-grade'}),
            'second_test_score': forms.TextInput(attrs={'class': 'final-grade'}),
            'exam_score': forms.TextInput(attrs={'class': 'final-grade'}),
            'out_of': forms.TextInput(attrs={'class': 'final-grade'}),
            'term': forms.Select(attrs={'class': 'final-grade'}),
            'first_test_grade': forms.Select(attrs={'class': 'final-grade'}),
            'second_test_grade': forms.Select(attrs={'class': 'final-grade'}),
            'exam_grade': forms.Select(attrs={'class': 'final-grade'}),
            'final_grade': forms.Select(attrs={'class': 'final-grade'}),
            'year': forms.Select(attrs={'class': 'final-grade'}),
        }

    def __init__(self, *args, **kwargs):
        class_info = kwargs.pop('class_info', None)
        teacher = kwargs.pop('teacher', None)
        super().__init__(*args, **kwargs)

        if class_info and teacher:
            self.fields['subject'].queryset = Subject.objects.filter(
                teacher_subject__teacher=teacher,
                teacher_subject__class_name=class_info
            )

class StudentPositionForm(forms.ModelForm):
    class Meta:
        model = StudentPosition
        fields = ['position', 'comment']
        widgets = {
            'position': forms.TextInput(attrs={'class': 'final-grade'}),
            'comment': forms.Textarea(attrs={'class': 'final-grade'}),
        }



class SchemeOfWorkForm(forms.ModelForm):
    class Meta:
        model = SchemeOfWork
        fields = ['term', 'subject', 'subject_date', 'subject_topics', 'week']
        widgets = {
            'term': forms.Select(attrs={'class': 'final-grade'}),
            'subject': forms.Select(attrs={'class': 'final-grade'}),
            'subject_date' : forms.TextInput(attrs={'class': 'final-grade'}),
            'subject_topics' : forms.Textarea(attrs={'class': 'final-grade'}),
            'week' : forms.TextInput(attrs={'class': 'final-grade'}),
        }


    def __init__(self, *args, **kwargs):
        class_info = kwargs.pop('class_info', None)
        teacher = kwargs.pop('teacher', None)
        super().__init__(*args, **kwargs)

        if class_info and teacher:
            # Filter subjects to only include those taught by the teacher in the specific class
            self.fields['subject'].queryset = Subject.objects.filter(
                teacher_subject__teacher=teacher,
                teacher_subject__class_name=class_info
            )