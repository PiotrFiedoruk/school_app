from school_app.models import Subject, Teacher, SchoolClass
from rest_framework import serializers


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class ClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SchoolClass
        field = '__all__'