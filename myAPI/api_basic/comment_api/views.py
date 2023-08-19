from rest_framework import generics, permissions
from rest_framework.filters import OrderingFilter, SearchFilter
from api_basic.comment_api.paginations import CommentPagination
from api_basic.models import Comment
from api_basic.comment_api.permissions import IsOwnerOrReadOnly
from api_basic.comment_api import serializers

class CommentList(generics.ListAPIView):
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['modified', 'author']
    search_fields = ['body']

    serializer_class= serializers.CommentSimpleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = CommentPagination

    def get_queryset(self):
        return Comment.objects.all().order_by('-modified')

class CommentDetail(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class= serializers.CommentCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

class CommentUpdate(generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    
    def perform_update(self, serializer):
        serializer.save(modified_by = self.request.user)

class CommentDestroy(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]