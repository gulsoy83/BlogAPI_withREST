from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from api_basic.user_api import serializers
from django.contrib.auth.models import User

from api_basic.user_api.paginations import UserPagination

class UserList(generics.ListAPIView):
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['username', 'date_joined']
    search_fields = ['username', 'email']

    serializer_class = serializers.UserSimpleSerializer
    pagination_class = UserPagination
    
    def get_queryset(self):
        return User.objects.all().order_by('-date_joined')

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer