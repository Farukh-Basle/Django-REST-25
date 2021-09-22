from django.shortcuts import render
from .models import Emp
from .serializers import EmpSerializer
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class EmpListView(generics.ListCreateAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

class EmpDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)