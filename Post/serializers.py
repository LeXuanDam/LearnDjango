from rest_framework import serializers
from Post.models import Post

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, default='')


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField()
    name = serializers.CharField(max_length=100, default='')
    file = serializers.CharField(max_length=100, default='')
    category_id = serializers.IntegerField()
    category = CategorySerializer(required=False)
    def create(self, validated_data):
        """
        Create and return a new `Post` instance, given the validated data.
        """
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Post` instance, given the validated data.
        """
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.name = validated_data.get('name', instance.name)
        instance.file = validated_data.get('file', instance.file)
        instance.save()
        return instance
