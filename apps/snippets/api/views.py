from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from apps.snippets.api.serializers import SnippetModelSerializer, SnippetListSerializer
from apps.snippets.models import Snippet
from apps.shared.mixins import SerializerClassMixin


class SnippetViewSet(SerializerClassMixin, ModelViewSet):
    """
    ModelViewSet for Snippet, Can perform CRUD
    """
    # permission_classes = (IsAuthenticated,)
    queryset = Snippet.objects.all()
    serializer_class = SnippetModelSerializer
    serializer_action_classes = {
        'list': SnippetListSerializer,
    }

    def perform_create(self, serializer):
        """
        set logged in user as user while creating a Snippet instance
        """
        serializer.save(user=self.request.user)


