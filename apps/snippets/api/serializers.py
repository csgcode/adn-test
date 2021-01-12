from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from rest_framework import serializers
from apps.snippets.models import Snippet


class SnippetModelSerializer(ModelSerializer):
    """
    Basic model serializer for Snippet model
    """
    class Meta:
        model = Snippet
        fields = '__all__'


class SnippetListSerializer(HyperlinkedModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='snippets:snippets-detail')

    class Meta:
        model = Snippet
        fields = ('id', 'link')
