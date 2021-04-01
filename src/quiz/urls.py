from django.urls import path
from rest_framework import routers

from .views import CategoryList, CategoryDetail, QuizDetail, DownloadView

urlpatterns = [
    path('', CategoryList.as_view(), name='category'),
    path('dl/', DownloadView.as_view()),
    # path('<category>/', CategoryDetail.as_view(), name='quiz'),
    path('question/<title>/', QuizDetail.as_view(), name='question'),
]
