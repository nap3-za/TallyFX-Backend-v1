from django.conf import settings
from rest_framework import serializers

from .models import (
	Trade
)


class TradeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Trade
		fields = (
			"id",
			"risk_appetite",
			"riskreward_profile",
			"order_type",
			"fill_price",
			"stoploss_price",
			"takeprofit_price",
			"execution_time",
			"exit_time",

			"outcome",
			"trade_review",
			
			# Relational fields
			"journal",
			"trading_model",
			"entry_model",
		)
		read_only_fields = (
			"id",
		)
		depth = 1

	def update(self, instance, validated_data):
		instance = instance.update(**validated_data)
		return instance




class ShortTradeSerializer(serializers.ModelSerializer):
	pandl							= serializers.DecimalField(source="net_profit_loss", max_digits=2, decimal_places=2)

	class Meta:
		model = Trade
		fields = (
			"id",
			"symbol",
			"riskreward_profile",
			"order_type",
			"outcome",

			"pandl",
		)
		read_only_fields = (
			"id",
			"symbol",
			"riskreward_profile",
			"order_type",
			"outcome",

			"pandl",
		)


