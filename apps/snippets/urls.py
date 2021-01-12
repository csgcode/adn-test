from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from apps.snippets.api.views import SnippetViewSet

app_name = 'snippets'

router = DefaultRouter()
router.register(r'snippets', SnippetViewSet, basename='snippets')

urlpatterns = [
    path('', include(router.urls)),
]
