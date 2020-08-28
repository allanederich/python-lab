# from django.urls import path
from django.conf.urls import url,include

from rest_framework_nested import routers
from .api import CustomerViewSet,BookViewSet

api_router = routers.DefaultRouter()
api_router.register(r"customers", CustomerViewSet)
api_router.register(r"books", BookViewSet)
# api_router.register(r"books/{pk}/reserve", BookViewSet)

customers_router = routers.NestedDefaultRouter(
    api_router, r"customers", lookup="customer")
customers_router.register(r"books", BookViewSet,
    basename="customer-books")

urlpatterns = [
    url("api/", include(api_router.urls)),
    url("api/", include(customers_router.urls)),
]