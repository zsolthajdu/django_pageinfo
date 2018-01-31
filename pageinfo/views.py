#from django.shortcuts import render
#from rest_framework import generics
#from rest_framework import permissions

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers  import PageInfoSerializer


#
#
#
class PageInfoViewSet( viewsets.ViewSet ):
	serializer_class = PageInfoSerializer;

	def create(self, request):
		serializer = PageInfoSerializer(data=request.data)
		if serializer.is_valid():
			pageinfo = serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)