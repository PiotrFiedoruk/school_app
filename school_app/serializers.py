from school_app.models import Subject, Teacher
from rest_framework import serializers


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'