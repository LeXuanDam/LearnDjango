from rest_framework import serializers
from Post.models import Post



class PostSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    user_id = serializers.IntegerField()
    category_id = serializers.IntegerField()
    name = serializers.CharField(max_length=100, default='')
    file = serializers.CharField(max_length=100, default='')
    # category = CategorySerializer()

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
        instance.category_id = validated_data.get('category_id', instance.code)
        instance.name = validated_data.get('name', instance.name)
        instance.file = validated_data.get('file', instance.file)
        instance.save()
        return instance
