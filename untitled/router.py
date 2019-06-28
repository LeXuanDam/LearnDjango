# from snippets.viewsets import SnippetViewset
from Post.viewsets import PostViewSet
from rest_framework import routers

router = routers.DefaultRouter()
# router.register('snippets', SnippetViewset)
router.register('post', PostViewSet, basename='post')
