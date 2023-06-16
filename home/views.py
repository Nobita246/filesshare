from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FilesSerializer
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


class FilesAPIView(APIView):

    def post(self, request):
        data = request.data
        print(data)
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
