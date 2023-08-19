from rest_framework import generics, permissions
from rest_framework.filters import OrderingFilter, SearchFilter
from api_basic.models import Post
from api_basic.post_api import serializers
from api_basic.post_api.paginations import PostPagination
from api_basic.post_api.permissions import IsOwnerOrReadOnly

class PostList(generics.ListAPIView):
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['publish', 'title']
    search_fields = ['body', 'title']
    
    serializer_class = serializers.PostSimpleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    
    pagination_class = PostPagination

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-publish')
        #queryset = queryset.filter(draft=False)
        return queryset

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,]
    lookup_field='slug'

class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all().order_by('-publish')
    serializer_class = serializers.PostCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

class PostUpdate(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,]
    def perform_update(self, serializer):
        serializer.save(modified_by = self.request.user)
    lookup_field='slug'

class PostDestroy(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,]
    lookup_field='slug'