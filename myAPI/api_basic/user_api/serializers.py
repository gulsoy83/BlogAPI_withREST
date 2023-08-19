from rest_framework import serializers
from django.contrib.auth.models import User

from api_basic.post_api.serializers import PostSimpleSerializer
from api_basic.comment_api.serializers import CommentSimpleSerializer

class UserSerializer(serializers.ModelSerializer):
    posts_ownedbyuser = PostSimpleSerializer(many=True, required=False)
    comments_ownedbyuser = CommentSimpleSerializer(many=True, required=False)
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'is_superuser', 'posts_ownedbyuser', 'comments_ownedbyuser']

class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username']