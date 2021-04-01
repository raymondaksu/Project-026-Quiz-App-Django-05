from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponse
from rest_framework import generics
from .models import Category, Question, Quiz
from .serializers import CategorySerializer, CategoryDetailSerializer, QuestionSerializer
from .pagination import MyPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.authentication import TokenAuthentication, SessionAuthentication

import mimetypes
from rest_framework.decorators import api_view, permission_classes, action
from django.http import FileResponse
from wsgiref.util import FileWrapper
from rest_framework_files.viewsets import ImportExportModelViewSet
from rest_framework.parsers import JSONParser, MultiPartParser
import os

class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [AllowAny]
    # authentication_classes = [TokenAuthentication, SessionAuthentication]

class CategoryDetail(generics.ListAPIView):
    serializer_class = CategoryDetailSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Quiz.objects.all()
        category = self.kwargs["category"]
        queryset = queryset.filter(category__name=category)
        return queryset

class QuizDetail(generics.ListAPIView):
    serializer_class = QuestionSerializer
    pagination_class = MyPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Question.objects.all()
        title = self.kwargs["title"]
        queryset = queryset.filter(quiz__title=title)
        return queryset

class DownloadView(generics.ListAPIView):
    permission_classes = [AllowAny]
    def get_queryset(self):
        queryset = 'return data'
        return queryset

    # file_path = '../staticfiles/download_files/'
    # if os.path.exists(file_path):
    #     with open(file_path, 'rb') as fh:
    #         response = HttpResponse(fh.read(), content_type="application/zip")
    #         name = "Redis-x64-3.0.504.zip"
    #         response['Content-Disposition'] = "attachment; filename=%s" % name
    #         return response

    # filename = '../staticfiles/download_files/Redis-x64-3.0.504.zip'
    # renderer classes used to render your content. will determine the file type of the download
    # renderer_classes = (JSONParser, )
    # parser_classes = (MultiPartParser, )
    # parser classes used to parse the content of the uploaded file
    # file_content_parser_classes = (JSONParser, )

    # zip_file = open('../staticfiles/download_files/Redis-x64-3.0.504.zip', 'rb')
    # response = HttpResponse(FileWrapper(zip_file), content_type='application/zip')
    # response['Content-Disposition'] = 'attachment; filename="%s"' % 'Redis-x64-3.0.504.zip'
    # return response

    # filename = '../staticfiles/download_files/Redis-x64-3.0.504.zip'
    # response = FileResponse(open(filename, 'rb'))
    # return response