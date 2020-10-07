from django.urls import path
from . import views


urlpatterns = [
    path('', views.TeacherListAPIView.as_view(), name="teachers"),
    path('<int:id>', views.TeacherDetailAPIView.as_view(), name="teacher"),
]
