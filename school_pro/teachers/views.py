from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import TeacherSerializer
from .models import Teacher
from rest_framework import permissions
from .permissions import IsOwner


class TeacherListAPIView(ListCreateAPIView):
    serializer_class = TeacherSerializer
    queryset = Expense.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class TeacherDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = Teacher.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
