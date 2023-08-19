from django.conf.global_settings import DATETIME_INPUT_FORMATS
from rest_framework import serializers
from api_basic.models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    modified_by = serializers.ReadOnlyField(source='modified_by.username')

    publish = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")
    modified = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")
    class Meta:
        model = Post
        extra_kwargs = {'url': {'lookup_field': 'slug'}}
        fields = ['url', 'id', 'title', 'image', 'body', 'draft', 'publish', 'author', 'modified', 'modified_by', 'comments_linkedtothispost']

class PostSimpleSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        #url = serializers.HyperlinkedIdentityField(view_name='post_api:post-detail', lookup_field='slug')
        extra_kwargs = {'url': {'lookup_field': 'slug'}}
        fields = ['url', 'author']

class PostCreateUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        extra_kwargs = {'url': {'lookup_field': 'slug'}}
        fields = ['url', 'title', 'image', 'body', 'draft']