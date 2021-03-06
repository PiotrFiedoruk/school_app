from school_app.models import Subject
from rest_framework import serializers


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'