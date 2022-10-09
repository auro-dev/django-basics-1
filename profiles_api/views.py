from email import message
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers


class HelloAPIView(APIView):
    """Demo API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns list of API views features"""

        api_view = [
            'This have many mehtods like get, put , patch, post, delete',
            'Is similar to django view',
            'gives you superpower of customisaation',
            'mapped manually with urls'
        ]

        return Response({'message': 'Hello!','api_view':api_view})

    def post(self, request, format=None):
        """Create a  hello msgg"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({"message": message})
        else:
            return Response(
                serializer.errors, 
                status = status.HTTP_400_BAD_REQUEST,
            )
     
    def put(self, request, pk=None):
        """Create a  hello msgg"""
        return Response({"method": "PUT"})
    
    def patch(self, request, pk=None):
        """Create a  hello msgg"""
        return Response({"method": "PATCH"})

    
    def delete(self, request, pk=None):
        """Create a  hello msgg"""
        return Response({"method": "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """Test APi view set"""

    def list(self, request):
        """Return a hello message"""
        
        a_viewset = [
            "User actions (list, create , view)",
            "Auto maps urls using router",
            "More functionality with less code"
        ]

        return Response({"message" : "Hello!", "a_viewset": a_viewset})

    def create(self, request):
        """Create a  hello msgg"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({"message": message})
        else:
            return Response(
                serializer.errors, 
                status = status.HTTP_400_BAD_REQUEST,
            )


    def retrieve(self, request, pk=None):
        """Get object by its id"""
        return Response({"http_method": "GET"})

    def update(self, request, pk=None):
        """Update an object"""
        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk=None):
        """Handle partial update"""
        return Response({"http_method": "PATCH"})

    def delete(self, request, pk=None):
        """Remove an object"""
        return Response({"http_method": "DELETE"})