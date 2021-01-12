from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from apps.shared.api.views import TagsListView, TagsSnippetDetailView

app_name = 'tags'

urlpatterns = [
    path('tag-snippet/', TagsSnippetDetailView.as_view(), name='tag_snippets'),
    path('tags-list/', TagsListView.as_view(), name='tags_list')
]
