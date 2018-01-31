
from rest_framework import routers
from django.conf.urls import url, include
from .views import PageInfoViewSet

router = routers.DefaultRouter()
router.register(r'', PageInfoViewSet, base_name='pageinfo')

# https://medium.com/django-rest-framework/django-rest-framework-viewset-when-you-don-t-have-a-model-335a0490ba6f

urlpatterns = [
	url(r'^pageinfo/', include(router.urls))
]
