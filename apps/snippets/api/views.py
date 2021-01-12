from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from apps.snippets.api.serializers import SnippetModelSerializer



class SnippetViewSet(ModelViewSet):
    """
    ModelViewSet for Snippet, Can perform CRUD
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = SnippetModelSerializer

