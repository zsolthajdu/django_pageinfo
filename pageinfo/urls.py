
from rest_framework import routers
from django.conf.urls import url, include
from .views import PageInfoViewSet

router = routers.DefaultRouter()
router.register(r'', PageInfoViewSet, basename='pageinfo')

urlpatterns = router.urls
