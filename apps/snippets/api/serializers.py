from rest_framework.serializers import ModelSerializer

from apps.snippets.models import Snippet


class SnippetModelSerializer(ModelSerializer):
    """
    Basic model serializer for Snippet model
    """
    class Meta:
        model = Snippet
        fields = '__all__'