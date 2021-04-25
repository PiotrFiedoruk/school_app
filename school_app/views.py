from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from school_app.models import Subject, Teacher, SchoolClass, Student
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
        subject = Subject.objects.get(id=id)
        teachers = Teacher.objects.filter(subject=subject)
        return Response({'subject': subject, 'teachers': teachers})

class TeacherList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'teacher_list.html'

    def get(self, request):
        teachers = Teacher.objects.all()
        return Response({'teachers': teachers})

class TeacherDetails(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'teacher_details.html'

    def get(self, request, id):
        teacher = Teacher.objects.get(id=id)
        return Response({'teacher': teacher})

class ClassList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'class_list.html'

    def get(self, request):
        classes = SchoolClass.objects.all()
        return Response({'classes': classes})

class ClassDetails(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'class_details.html'

    def get(self, request, id):
        s_class = SchoolClass.objects.get(id=id)
        students = Student.objects.filter(school_class=s_class)
        return Response({'class': s_class, 'students': students})
