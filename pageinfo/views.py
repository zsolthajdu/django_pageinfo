
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers  import PageInfoSerializer
from rest_framework.decorators import detail_route, list_route

#
#
#
class PageInfoViewSet( viewsets.ViewSet ):
	serializer_class = PageInfoSerializer;

	def create(self, request, pk=None):
		serializer = PageInfoSerializer(data=request.data)
		if serializer.is_valid():
			pageinfo = serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
