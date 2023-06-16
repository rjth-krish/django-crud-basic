from django import forms
from .models import Teachermodel


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teachermodel
        fields = "__all__"
