from django.db import models
from django.db.models import Q

from core.apps.misc.field_choices import (
	OrderTypes,
	TradeOutcomes,

	RiskAppetites,
	RiskRewardProfiles,


)


class TradeQuerySet(models.QuerySet):
	
	def search(self, query=None):
		if query == None:
			return self.none()
		lookups += Q(Q(order_type__icontains=query) | Q(execution_time__icontains=query))
		return self.filter(lookups)

class Trade(models.Model):
	
	class TradeManager(models.Manager):

		def create(self, journal, trading_model, entry_model, risk_appetite, riskreward_profile, order_type, fill_price=None, stoploss_price=None, takeprofit_price=None, execution_time=None, exit_time=None):
			model = self.model(
				journal=journal,
				trading_model=trading_model,
				entry_model=entry_model,
				risk_appetite=risk_appetite,
				riskreward_profile=riskreward_profile,
				order_type=order_type,
				fill_price=fill_price,
				stoploss_price=stoploss_price,
				takeprofit_price=takeprofit_price,
				execution_time=execution_time,
				exit_time=exit_time,
			)
			model.save(using=self._db)
			return model

		def get_queryset(self):
			return TradeQuerySet(self.model, using=self._db)

		def search(self, query=None):
			return self.get_queryset().search(query=query)


	journal 						= models.ForeignKey(
		"trading_plan.Journal",
		related_name="trades",
		related_query_name="trade",
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
	)

	trading_model 						= models.ForeignKey(
		"trading_plan.TradingModel",
		related_name="trades",
		related_query_name="trade",
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
	)

	entry_model 						= models.ForeignKey(
		"trading_plan.EntryModel",
		related_name="trades",
		related_query_name="trade",
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
	)

	risk_appetite						= models.CharField(verbose_name="risk appetite", choices=RiskAppetites.choices, max_length=3, null=False, blank=False)
	riskreward_profile 					= models.CharField(verbose_name="reward profile", choices=RiskRewardProfiles.choices, max_length=3, null=False, blank=False)

	order_type 							= models.CharField(verbose_name="order type", choices=OrderTypes.choices, max_length=3, null=False, blank=False)
	fill_price 							= models.DecimalField(verbose_name="fill price", max_digits=7, decimal_places=5, null=True, blank=True)
	stoploss_price 						= models.DecimalField(verbose_name="fill price", max_digits=7, decimal_places=5, null=True, blank=True)
	takeprofit_price 					= models.DecimalField(verbose_name="fill price", max_digits=7, decimal_places=5, null=True, blank=True)
	execution_time						= models.DateTimeField(verbose_name="execution time", auto_now_add=False, null=True, blank=True)
	exit_time 							= models.DateTimeField(verbose_name="exit time", auto_now_add=False, null=True, blank=True)

	outcome 		 					= models.CharField(verbose_name="outcome", choices=TradeOutcomes.choices, max_length=3, default=TradeOutcomes.IN_PROGRESS, null=False, blank=False)
	trade_review 						= models.CharField(verbose_name="trade review", max_length=250, null=True, blank=True)

	rules_observed 						= models.BooleanField(verbose_name="rulse oberved", default=True)

	timestamp							= models.DateTimeField(auto_now_add=True)

	objects = TradeManager()


	def __str__(self):
		return f"{self.id}"


	def update(self, **kwargs):
		Trade.objects.filter(id=self.id).update(**kwargs)
		return Trade.objects.get(id=self.id)


	@property
	def net_profit_loss(self):
		return 70
	
	@property
	def duration(self):
		return 70
	
	@property
	def trading_session(self):
		return 70
	
