from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from apps.shared.api.serializers import TagsModelSerializer
from apps.snippets.api.serializers import SnippetModelSerializer
from apps.snippets.models import Snippet
from apps.shared.models import Tag


class TagsListView(ListAPIView):
    """
    Model List for Snippet, Can perform CRUD
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = TagsModelSerializer
    queryset = Tag.objects.all()


class TagsSnippetDetailView(GenericAPIView):
    """
    Accepts a query param og Tag `id`, returns the response of filtered Snippets matching the id
    """
    serializer_class = SnippetModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Snippet.objects.all()

    def get(self, request):
        pk = request.GET.get('id', None)
        instance = get_object_or_404(Tag, pk=pk)
        queryset = self.get_queryset().filter(tag=instance)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
