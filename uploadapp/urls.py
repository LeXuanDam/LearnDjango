from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('upload/', views.FileUploadView.as_view()),
    # path('snippets/<int:pk>', views.snippet_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)
