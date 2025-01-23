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
	TradeSerializer,
)
from .models import (
	Trade,
)



class TradeViewSetPagination(pagination.PageNumberPagination):
	page_size = 10
	page_size_query_param = "size"
	max_page_size = 25

class TradeViewSet(viewsets.ModelViewSet):

	queryset = Trade.objects.all()
	serializer_class = TradeSerializer
	pagination_class = TradeViewSetPagination

