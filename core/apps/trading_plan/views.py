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
from core.apps.trade.serializers import ShortTradeSerializer

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

	queryset = Journal.objects.all().order_by("-title")
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

	
class DefaultJournalData(generics.GenericAPIView):

	def get(self, request, *args, **kwargs):
		journal = None
		
		if Journal.objects.all().count() > 0:
			try:
				journal = Journal.objects.get(default_journal=True)
			except:

				return Response({"error": "Invalid journal code"}, status=status.HTTP_400_BAD_REQUEST)
		
			serialized_recent_trades = []
			for trade in journal.recent_trades:
				serializer_class.append({
					**ShortTradeSerializer(trade).data,
					"model": str(trade.model),
				})

			response_data = {
				"id": journal.id,
				"title": journal.title,
				"code": journal.code,
				"netReturns": journal.net_return,

				"recentTrades": serialized_recent_trades,
			}

		else:
			return Response(None, status=status.HTTP_204_NO_CONTENT)

		return Response(response_data, status=status.HTTP_200_OK)

