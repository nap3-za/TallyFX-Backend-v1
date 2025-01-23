from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name="trading_plan"


urlpatterns = [
]


journal_router = DefaultRouter()
journal_router.register("journal", views.JournalViewSet, basename="journal")
urlpatterns += journal_router.urls

trading_model_router = DefaultRouter()
trading_model_router.register("trading-model", views.TradingModelViewSet, basename="trading-model")
urlpatterns += trading_model_router.urls

market_conditions_router = DefaultRouter()
market_conditions_router.register("market-conditions", views.MarketConditionsViewSet, basename="market-conditions")
urlpatterns += market_conditions_router.urls

entry_model_router = DefaultRouter()
entry_model_router.register("entry-model", views.EntryModelViewSet, basename="entry-model")
urlpatterns += entry_model_router.urls
