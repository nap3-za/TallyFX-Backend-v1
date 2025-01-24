from django.conf import settings
from rest_framework import serializers

from .models import (
	Journal,
	TradingModel,
	EntryModel,
	MarketConditions,
)


class JournalSerializer(serializers.ModelSerializer):

	class Meta:
		model = Journal
		fields = (
			"id",
			"title",
			"code",
			"adages",

			# Relational field
			"target_profile",
		)
		read_only_fields = (
			"id",
		)
		depth = 1

	def update(self, instance, validated_data):
		instance = instance.update(**validated_data)
		return instance


class TradingModelSerializer(serializers.ModelSerializer):

	class Meta:
		model = TradingModel
		fields = (
			"id",
			"title", "code",
			"preffered_days", "preffered_session", "preffered_hour",
			"positive_price_market_signatures", "negative_price_market_signatures",
			"trading_style",
			"risk_appetite", "riskreward_profile", "avg_duration",
			"win_rate", "breakeven_rate", "reversal_rate", "avg_return", "avg_loss",
			
			# Relational fields
			"routines",
			"market_conditions",
		)
		read_only_fields = (
			"id",
		)

		depth = 1

	def update(self, instance, validated_data):
		instance = instance.update(**validated_data)
		return instance


class MarketConditionsSerializer(serializers.ModelSerializer):

	class Meta:
		model = MarketConditions
		fields = (
			"id",
			"general_classification",
			"price_signatures",
		)
		read_only_fields = (
			"id",
		)

	def update(self, instance, validated_data):
		instance = instance.update(**validated_data)
		return instance


class EntryModelSerializer(serializers.ModelSerializer):

	class Meta:
		model = EntryModel
		fields = (
			"id",
			"title",
			"code",
			"price_market_triggers",
		)
		read_only_fields = (
			"id",
		)

	def update(self, instance, validated_data):
		instance = instance.update(**validated_data)
		return instance


