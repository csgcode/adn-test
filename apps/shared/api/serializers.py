from rest_framework.serializers import ModelSerializer

from apps.shared.models import Tag


class TagsModelSerializer(ModelSerializer):
    """
    Basic model serializer for Tags model
    """
    class Meta:
        model = Tag
        fields = '__all__'

