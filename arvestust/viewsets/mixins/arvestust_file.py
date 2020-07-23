from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response


class ArvestustFileMixin(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.get_for_user(
            user=self.request.user
        )

    @action(detail=False, methods=['get'])
    def me(self, request):
        objects = self.queryset.objects.filter(author=request.user)

        page = self.paginate_queryset(objects)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(objects, many=True)
        return Response(serializer.data)
