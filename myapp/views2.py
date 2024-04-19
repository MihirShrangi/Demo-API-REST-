from . import models,serializers
from rest_framework import generics



class EmpListView(generics.ListCreateAPIView):
    queryset=models.Emp.objects.all()
    serializer_class=serializers.EmpSerializer

class EmpDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Emp.objects.all()
    serializer_class=serializers.EmpSerializer