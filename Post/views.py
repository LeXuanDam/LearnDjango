from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Post.models import Post
from Post.serializers import PostSerializer
from django.core.files.storage import FileSystemStorage
from django.core import serializers
import json


@api_view(['GET', 'POST'])

def post_list(request):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        context = {}
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        request.data['file'] = context['url']
        request.data['user_id'] = 1
        # request.data['category_id'] = 1
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)