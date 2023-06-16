from rest_framework import serializers
from teachers.models import Teachermodel


class and_serializers(serializers.ModelSerializer):
    class Meta:
        model = Teachermodel
        fields = '__all__'
