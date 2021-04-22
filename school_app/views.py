from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from school_app.models import Subject, Teacher
from school_app.serializers import SubjectSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'subjects': reverse('subjects-list', request=request, format=format)
    })


# class SubjectList(generics.ListCreateAPIView):
#     queryset = Subject.objects.all()
#     serializer_class = SubjectSerializer

# class SubjectDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Subject.objects.all()
#     serializer_class = SubjectSerializer

class SubjectList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'subject_list.html'

    def get(self, request):
        subjects = Subject.objects.all()
        teachers = Teacher.objects.all()
        return Response({'subjects': subjects, 'teachers': teachers})

class SubjectDetails(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'subject_details.html'

    def get(self, request, id):
        subject = Subject.objects.filter(pk=id)
        return Response({'subject': subject})





