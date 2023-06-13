from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FilesSerializer

# Create your views here.


class FilesAPIView(APIView):

    def post(self, request):
        data = request.data
        serializer = FilesSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": 200,
                "message": "Files Uploaded Successfully!",
                "data": serializer.data
            })

        return Response({
            "status": 400,
            "message": "Somthing Went Wrong!",
            "errors": serializer.errors
        })
