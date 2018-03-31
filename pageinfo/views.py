
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers  import PageInfoSerializer
from rest_framework.decorators import detail_route, list_route
from .pageinfo import PageInfo

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

	def list(self, request ):
		"""
		Returns pageinfo if a url is requested, the default otherwise
		"""
		inUrl = request.query_params.get('url', None )
		#if inUrl is None:
		#	inUrl = 'https://google.com'
		serializer = PageInfoSerializer( instance = PageInfo(url=inUrl), many=False )
		return Response( serializer.data )

	def retrieve(self, request, pk=None):
		"""
		Returns pageinfo if a url is requested, the default otherwise
		"""
		try:
			inUrl = request.query_params.get('url', None )
			#if inUrl is None:
			#	inUrl = 'https://google.com'
			pageinfo = PageInfo( url=inUrl )
		except KeyError:
			return Response(status=status.HTTP_404_NOT_FOUND)
		except ValueError:
			return Response(status=status.HTTP_400_BAD_REQUEST)

		serializer = PageInfoSerializer(instance=pageinfo)
		return Response(serializer.data)

