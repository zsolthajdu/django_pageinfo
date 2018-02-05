
from rest_framework import routers
from django.conf.urls import url, include
from .views import PageInfoViewSet

router = routers.DefaultRouter()
router.register(r'pageinfo', PageInfoViewSet, base_name='pageinfo')

urlpatterns = router.urls
