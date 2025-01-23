from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name="trade"


urlpatterns = [
]


trade_router = DefaultRouter()
trade_router.register("trade", views.TradeViewSet, basename="trade")
urlpatterns += trade_router.urls