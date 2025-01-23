from rest_framework import (
	generics,
	status,
	pagination,
	mixins,
	viewsets,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
	JournalSerializer,
	TradingModelSerializer,
	EntryModelSerializer,
	MarketConditionsSerializer,
)
from .models import (
	Journal,
	TradingModel,
	EntryModel,
	MarketConditions,
)



class JournalViewSetPagination(pagination.PageNumberPagination):
	page_size = 10
	page_size_query_param = "size"
	max_page_size = 25

class JournalViewSet(viewsets.ModelViewSet):

	queryset = Journal.objects.all()
	serializer_class = JournalSerializer
	pagination_class = JournalViewSetPagination


class TradingModelViewSetPagination(pagination.PageNumberPagination):
	page_size = 10
	page_size_query_param = "size"
	max_page_size = 25

class TradingModelViewSet(viewsets.ModelViewSet):

	queryset = TradingModel.objects.all()
	serializer_class = TradingModelSerializer
	pagination_class = TradingModelViewSetPagination


class EntryModelViewSetPagination(pagination.PageNumberPagination):
	page_size = 10
	page_size_query_param = "size"
	max_page_size = 25


class EntryModelViewSet(viewsets.ModelViewSet):

	queryset = EntryModel.objects.all()
	serializer_class = EntryModelSerializer
	pagination_class = EntryModelViewSetPagination


class MarketConditionsViewSetPagination(pagination.PageNumberPagination):
	page_size = 10
	page_size_query_param = "size"
	max_page_size = 25


class MarketConditionsViewSet(viewsets.ModelViewSet):

	queryset = MarketConditions.objects.all()
	serializer_class = MarketConditionsSerializer
	pagination_class = MarketConditionsViewSetPagination

	