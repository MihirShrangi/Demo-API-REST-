from . import models,serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.http import Http404

# Create your views here.

class DeptListView(APIView):
    def get(self,request,format=None):
        deptdata=models.Dept.objects.all()
        ser=serializers.DeptSerializer(deptdata,many=True)
        return Response(ser.data,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        ser=serializers.DeptSerializer(data = request.data)
        if ser.is_valid():
            ser.save();
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors)
    
class DeptDetailView(APIView):
    def getDept(self,pk):
        try:
            data=models.Dept.objects.get(pk=pk);
            return data
        except:
            raise Http404
        
    def get(self,request,pk,format=None):
        data=self.getDept(pk)
        ser=serializers.DeptSerializer(data)
        return Response(ser.data,status=status.HTTP_200_OK)

    def put(self,request,pk,format=None):
        data=self.getDept(pk)
        ser=serializers.DeptSerializer(data,data=request.data)
        if ser.is_valid():
            ser.save();
            return Response(ser.data,status=status.HTTP_202_ACCEPTED)
        return Response(ser.errors)

    def delete(self,request,pk,format=None):
        data=self.getDept(pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)