from snippets.models import Snippet
from .serializers import SnippetsSerializer
from rest_framework import viewsets

class SnippetViewset(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetsSerializer