from rest_framework import serializers
from api_basic.models import Comment
from api_basic.post_api.serializers import PostSimpleSerializer

class CommentSerializer(serializers.ModelSerializer):
    masterPost = PostSimpleSerializer(many=False, required=True)
    author = serializers.ReadOnlyField(source='author.username')
    modified_by = serializers.ReadOnlyField(source='modified_by.username')

    publish = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")
    modified = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")
    class Meta:
        model = Comment
        fields = ['url', 'id', 'body', 'masterPost', 'masterComment', 'publish', 'author', 'modified', 'modified_by' ]

class CommentSimpleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Comment
        fields = ['url', 'author']

class CommentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['url', 'body', 'masterPost', 'masterComment']