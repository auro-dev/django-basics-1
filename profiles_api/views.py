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




class PostAPIView(APIView):
    """Post API View"""

    serializer_class = serializers.UserPostsSerializer

    def get(self, request, format=None):
        """Returns list of API views features"""

        api_view = [
            'This have many mehtods like get, put , patch, post, delete',
            'Is similar to django view',
            'gives you superpower of customisaation',
            'mapped manually with urls'
        ]

        return Response({'message': 'Posts!','api_view': api_view})

    def post(self, request, format=None):
        """Create a  post"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            title = serializer.validated_data.get('title')
            url = serializer.validated_data.get('url')
            return Response({"title": title, "url" : url})
        else:
            return Response(
                serializer.errors, 
                status = status.HTTP_400_BAD_REQUEST,
            )
     
    def put(self, request, pk=None):
        """Put post"""
        return Response({"method": "PUT"})
    
    def patch(self, request, pk=None):
        """Patch / edit posts"""
        return Response({"method": "PATCH"})

    
    def delete(self, request, pk=None):
        """delete a post"""
        return Response({"method": "Post deleted successfully"})


class CityViewSet(viewsets.ViewSet):
    """Test APi view set"""

    def list(self, request):
        """Return a city llits"""
        
        a_viewset = [
            "User actions (list, create , view)",
            "Auto maps urls using router",
            "More functionality with less code",
            "More posts"
        ]

        return Response({"message" : "Hello!", "a_viewset": a_viewset})

    def create(self, request):
        """Create a  Posts"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response({"name": name})
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




class CityAPIView(APIView):
    """City API View"""

    serializer_class = serializers.CitiesSerializer

    def get(self, request, format=None):
        """Returns list of API views features"""

        api_view = [
            'This have many mehtods like get, put , patch, post, delete',
            'Is similar to django view',
            'gives you superpower of customisaation',
            'mapped manually with urls'
        ]

        return Response({'message': 'Posts!','api_view': api_view})

    def post(self, request, format=None):
        """Create a  city"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response({"name": name})
        else:
            return Response(
                serializer.errors, 
                status = status.HTTP_400_BAD_REQUEST,
            )
     
    def put(self, request, pk=None):
        """Put post"""
        return Response({"method": "PUT"})
    
    def patch(self, request, pk=None):
        """Patch / edit posts"""
        return Response({"method": "PATCH"})

    
    def delete(self, request, pk=None):
        """delete a post"""
        return Response({"method": "Post deleted successfully"})
    
    
    
    

class FriendRequestSet(viewsets.ViewSet):
    """FriendRequestSet APi view set"""

    def list(self, request):
        """Return a friend request llits"""
        
        a_viewset = [
            "User actions (list, create , view)",
            "Auto maps urls using router",
            "More functionality with less code",
            "More posts"
        ]

        return Response({"message" : "Hello!", "a_viewset": a_viewset})

    def create(self, request):
        """Create a  Friend request"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            from = serializer.validated_data.get('from')
            to = serializer.validated_data.get('to')
            return Response({"from": from, "to" : to})
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




class FriendRequestAPIView(APIView):
    """FriendRequestAPIView API View"""

    serializer_class = serializers.FriendRequestsSerializer

    def get(self, request, format=None):
        """Returns list of API views features"""

        api_view = [
            'This have many mehtods like get, put , patch, post, delete',
            'Is similar to django view',
            'gives you superpower of customisaation',
            'mapped manually with urls'
        ]

        return Response({'message': 'Friend requests!','api_view': api_view})

    def post(self, request, format=None):
        """Create a  Friend request"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            from = serializer.validated_data.get('from')
            to = serializer.validated_data.get('to')
            return Response({"from": from, "to" : to})
        else:
            return Response(
                serializer.errors, 
                status = status.HTTP_400_BAD_REQUEST,
            )
     
    def put(self, request, pk=None):
        """Put post"""
        return Response({"method": "PUT"})
    
    def patch(self, request, pk=None):
        """Patch / edit posts"""
        return Response({"method": "PATCH"})

    
    def delete(self, request, pk=None):
        """delete a post"""
        return Response({"method": "Rquest deleted successfully"})
 





class HashTagSet(viewsets.ViewSet):
    """HashTagSet APi view set"""

    def list(self, request):
        """Return a friend request llits"""
        
        a_viewset = [
            "User actions (list, create , view)",
            "Auto maps urls using router",
            "More functionality with less code",
            "More posts"
        ]

        return Response({"message" : "Hello!", "a_viewset": a_viewset})

    def create(self, request):
        """Create a  Hash Tag"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response({"name": name})
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




class HashTagAPIView(APIView):
    """HashTag API View"""

    serializer_class = serializers.HashTagsSerializer

    def get(self, request, format=None):
        """Returns list of API views features"""

        api_view = [
            'This have many mehtods like get, put , patch, post, delete',
            'Is similar to django view',
            'gives you superpower of customisaation',
            'mapped manually with urls'
        ]

        return Response({'message': 'Friend requests!','api_view': api_view})

    def post(self, request, format=None):
        """Create a  Hash Tag"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response({"name": name})
        else:
            return Response(
                serializer.errors, 
                status = status.HTTP_400_BAD_REQUEST,
            )
     
    def put(self, request, pk=None):
        """Put post"""
        return Response({"method": "PUT"})
    
    def patch(self, request, pk=None):
        """Patch / edit posts"""
        return Response({"method": "PATCH"})

    
    def delete(self, request, pk=None):
        """delete a hash tag"""
        return Response({"method": "Hash Tag deleted successfully"})




class OrderSet(viewsets.ViewSet):
    """OrderSet APi view set"""

    def list(self, request):
        """Return a orders lists"""
        
        a_viewset = [
            "User actions (list, create , view)",
            "Auto maps urls using router",
            "More functionality with less code",
            "More posts"
        ]

        return Response({"items" : ["propaxine", "citramacic"], "a_viewset": a_viewset})

    def create(self, request):
        """Create a Order"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('items')
            return Response({"items": items})
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




class OrderAPIView(APIView):
    """Order API View"""

    serializer_class = serializers.OrdersSerializer

    def get(self, request, format=None):
        """Returns list of API views features"""

        api_view = [
            'This have many mehtods like get, put , patch, post, delete',
            'Is similar to django view',
            'gives you superpower of customisaation',
            'mapped manually with urls'
        ]

        return Response({'items': ["propaxine", "citramacic"],'api_view': api_view})

    def post(self, request, format=None):
        """Create a  Orders"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            items = serializer.validated_data.get('items')
            return Response({"items": items})
        else:
            return Response(
                serializer.errors, 
                status = status.HTTP_400_BAD_REQUEST,
            )
     
    def put(self, request, pk=None):
        """Put Order"""
        return Response({"method": "PUT"})
    
    def patch(self, request, pk=None):
        """Patch / edit Order"""
        return Response({"method": "PATCH"})

    
    def delete(self, request, pk=None):
        """delete a Order"""
        return Response({"method": "Order deleted successfully"})


