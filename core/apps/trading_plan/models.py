from django.db import models
from django.db.models import Q
from django.contrib.postgres.fields import ArrayField

from core.apps.misc.field_choices import (
	TradingStyles,
	Markets,

	GeneralMarketConditions,
	TradingDays,
	TradingHours,
	TradingSessions,

	RiskAppetites,
	RiskRewardProfiles,

)


class MarketConditionsQuerySet(models.QuerySet):
	
	def search(self, query=None):
		if query == None:
			return self.none()
		lookups += Q(Q(general_classification__icontains=query) | Q(price_signatures__icontains=query))
		return self.filter(lookups)

class MarketConditions(models.Model):
	
	class MarketConditionsManager(models.Manager):

		def create(self, general_classification, price_signatures):
			model = self.model(
				general_classification=general_classification,
				price_signatures=price_signatures,
			)
			model.save(using=self._db)
			return model

		def get_queryset(self):
			return MarketConditionsQuerySet(self.model, using=self._db)

		def search(self, query=None):
			return self.get_queryset().search(query=query)


	
	general_classification 		= models.CharField(verbose_name="general classification", choices=GeneralMarketConditions.choices, max_length=3, null=False, blank=False)
	market_structure 			= ArrayField(
									models.CharField(max_length=250,null=True, blank=True),
									size=25, null=True, blank=True
								)


	timestamp					= models.DateTimeField(auto_now_add=True)

	objects = MarketConditionsManager()


	def __str__(self):
		return f"{self.id}"
		

	def update(self, **kwargs):
		MarketConditions.objects.filter(id=self.id).update(**kwargs)
		return MarketConditions.objects.get(id=self.id)


class ObjectiveProfileQuerySet(models.QuerySet):
	
	def search(self, query=None):
		if query == None:
			return self.none()
		lookups += Q(Q(title__icontains=query) | Q(code__icontains=query))
		return self.filter(lookups)

class ObjectiveProfile(models.Model):
	
	class ObjectiveProfileManager(models.Manager):

		def create(self, title, code, daily_objective=None, weekly_objective=None, monthly_objective=None):
			model = self.model(
				title=title,
				code=code,
				daily_objective=daily_objective,
				weekly_objective=weekly_objective,
				monthly_objective=monthly_objective,
			)
			model.save(using=self._db)
			return model

		def get_queryset(self):
			return ObjectiveProfileQuerySet(self.model, using=self._db)

		def search(self, query=None):
			return self.get_queryset().search(query=query)


	title 						= models.CharField(verbose_name="title", max_length=125, null=False, blank=False)
	code						= models.CharField(verbose_name="code", max_length=15, unique=True, null=False, blank=False)

	# [ <drawdown>, <target>, <target_max> ]
	daily_objective				= ArrayField(
									models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True),
									size=1, null=True, blank=True
								)
	weekly_objective			= ArrayField(
									models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True),
									size=1, null=True, blank=True
								)
	monthly_objective			= ArrayField(
									models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True),
									size=1, null=True, blank=True
								)


	timestamp					= models.DateTimeField(auto_now_add=True)

	objects = ObjectiveProfileManager()


	def __str__(self):
		return f"{self.id}"
		

	def update(self, **kwargs):
		ObjectiveProfile.objects.filter(id=self.id).update(**kwargs)
		return ObjectiveProfile.objects.get(id=self.id)		


class TradeManagementQuerySet(models.QuerySet):
	
	def search(self, query=None):
		if query == None:
			return self.none()
		lookups += Q(Q(pre_trade__icontains=query) | Q(active_trade__icontains=query) | Q(post_trade__icontains=query) | Q(guidelines__icontains=query))
		return self.filter(lookups)

class TradeManagement(models.Model):
	
	class TradeManagementManager(models.Manager):

		def create(self, pre_trade, active_trade, post_trade, guidelines=None):
			model = self.model(
				pre_trade=pre_trade,
				active_trade=active_trade,
				post_trade=post_trade,
				guidelines=guidelines,
			)
			model.save(using=self._db)
			return model

		def get_queryset(self):
			return TradeManagementQuerySet(self.model, using=self._db)

		def search(self, query=None):
			return self.get_queryset().search(query=query)


	pre_trade					= ArrayField(
								models.CharField(max_length=125,null=True, blank=True),
								size=10, null=False, blank=False
							)
	active_trade				= ArrayField(
								models.CharField(max_length=125,null=True, blank=True),
								size=10, null=False, blank=False
							)
	post_trade					= ArrayField(
								models.CharField(max_length=125,null=True, blank=True),
								size=10, null=False, blank=False
							)
	guidelines					= ArrayField(
								models.CharField(max_length=125,null=True, blank=True),
								size=5, null=False, blank=False
							)


	timestamp					= models.DateTimeField(auto_now_add=True)

	objects = TradeManagementManager()


	def __str__(self):
		return f"{self.id}"
		

	def update(self, **kwargs):
		TradeManagement.objects.filter(id=self.id).update(**kwargs)
		return TradeManagement.objects.get(id=self.id)


class TradingPlanQuerySet(models.QuerySet):
	
	def search(self, query=None):
		if query == None:
			return self.none()
		lookups += Q(Q(title__icontains=query) | Q(code__icontains=query) | Q(trading_style__icontains=query))
		return self.filter(lookups)

class TradingPlan(models.Model):
	
	class TradingPlanManager(models.Manager):

		def create(self, title, code, trading_style, markets, routines=None, riskreward_profiles=None, adages=None):
			model = self.model(
				title=title,
				code=code,
				trading_style=trading_style,
				markets=markets,
				routines=routines,
				riskreward_profiles=riskreward_profiles,
				adages=adages,
			)
			model.save(using=self._db)
			return model

		def get_queryset(self):
			return TradingPlanQuerySet(self.model, using=self._db)

		def search(self, query=None):
			return self.get_queryset().search(query=query)


	title 						= models.CharField(verbose_name="title", max_length=125, null=False, blank=False)
	code						= models.CharField(verbose_name="code", max_length=15, unique=True, null=False, blank=False)

	trading_style 				= models.CharField(verbose_name="trading_style", choices=TradingStyles.choices, max_length=3, null=False, blank=False)
	markets 					= models.CharField(verbose_name="markets", choices=Markets.choices, max_length=3, null=False, blank=False)
	routines 					= models.ManyToManyField(
		"tasks.Routine",
		related_name="trading_plans",
		related_query_name="trading_plan",
		blank=True,
	)
	target_profile 				= models.ManyToManyField(
		"trading_plan.ObjectiveProfile",
		related_name="trading_plans",
		related_query_name="trading_plan",
		blank=True,
	)
	trading_week 				= ArrayField(
									models.CharField(default="Day-Off", null=False, blank=False),
									size=5, null=True, blank=True
								)

	trade_management 			= models.ForeignKey(
		"trading_plan.TradeManagement",
		related_name="trading_plans",
		related_query_name="trading_plan",
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
	)

	adages 						= ArrayField(models.CharField(max_length=125,null=True, blank=True), size=5, null=True, blank=True)


	timestamp					= models.DateTimeField(auto_now_add=True)

	objects = TradingPlanManager()


	def __str__(self):
		return f"{self.id}"

	def update(self, **kwargs):
		TradingPlan.objects.filter(id=self.id).update(**kwargs)
		return TradingPlan.objects.get(id=self.id)


class TradingModelQuerySet(models.QuerySet):
	
	def search(self, query=None):
		if query == None:
			return self.none()
		# - - -
		lookups += Q(Q(field__icontains=query))
		return self.filter(lookups)

class TradingModel(models.Model):
	
	class TradingModelManager(models.Manager):

		def create(self, field):
			model = self.model(
				# - - -
			)
			model.save(using=self._db)
			return model

		def get_queryset(self):
			return TradingModelQuerySet(self.model, using=self._db)

		def search(self, query=None):
			return self.get_queryset().search(query=query)



	market_conditions 					= models.ForeignKey(
		"trading_plan.MarketConditions",
		related_name="trading_models",
		related_query_name="trading_model",
		on_delete=models.PROTECT,
		null=True,
		blank=True,
	)

	preffered_days 						= ArrayField(
											models.CharField(max_length=3, choices=TradingDays.choices),
											size=5, null=False, blank=False
										)
	preffered_session 					= ArrayField(
											models.CharField(max_length=3, choices=TradingSessions.choices),
											size=5, null=False, blank=False
										)
	preffered_hour	 					= ArrayField(
											models.CharField(max_length=3, choices=TradingHours.choices),
											size=24, null=False, blank=False
										)

	positive_price_market_signatures	= ArrayField(
											models.CharField(max_length=250),
											size=25, null=False, blank=False
										)
	negative_price_market_signatures	= ArrayField(
											models.CharField(max_length=250),
											size=25, null=False, blank=False
										)

	risk_appetite						= models.CharField(verbose_name="risk appetite", choices=RiskAppetites.choices, max_length=3, null=False, blank=False)
	riskreward_profile 					= models.CharField(verbose_name="reward profile", choices=RiskRewardProfiles.choices, max_length=3, null=False, blank=False)
	avg_duration						= models.DurationField(verbose_name="average duration", null=False, blank=False)

	# Displayed as theoreticals on the frontend
	win_rate							= models.DecimalField(verbose_name="win rate", max_digits=3, decimal_places=2, null=True, blank=True),
	breakeven_rate						= models.DecimalField(verbose_name="breakeven rate", max_digits=3, decimal_places=2, null=True, blank=True),
	reversal_rate						= models.DecimalField(verbose_name="reversal rate", max_digits=3, decimal_places=2, null=True, blank=True),
	avg_return 							= models.DecimalField(verbose_name="average return", max_digits=3, decimal_places=2, null=True, blank=True),
	avg_loss  							= models.DecimalField(verbose_name="average loss", max_digits=3, decimal_places=2, null=True, blank=True),

	trading_plan 						= models.ForeignKey(
		"trading_plan.TradingPlan",
		related_name="trading_models",
		related_query_name="trading_model",
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
	)

	timestamp							= models.DateTimeField(auto_now_add=True)

	objects = TradingModelManager()


	def __str__(self):
		return f"{self.id}"
		

	def update(self, **kwargs):
		TradingModel.objects.filter(id=self.id).update(**kwargs)
		return TradingModel.objects.get(id=self.id)

	@property
	def actual_win_rate(self):
		return 60

	@property
	def actual_breakeven_rate(self):
		return 70
		
	@property
	def actual_reversal_rate(self):
		return 70

	@property
	def actual_return(self):
		return 70

	@property
	def actual_avg_loss(self):
		return 70
	
	


class EntryModelQuerySet(models.QuerySet):
	
	def search(self, query=None):
		if query == None:
			return self.none()
		lookups += Q(Q(title__icontains=query) | Q(code__icontains=query))
		return self.filter(lookups)

class EntryModel(models.Model):
	
	class EntryModelManager(models.Manager):

		def create(self, price_market_triggers, title, code):
			model = self.model(
				title=title,
				code=code,
				price_market_triggers=price_market_triggers,
			)
			model.save(using=self._db)
			return model

		def get_queryset(self):
			return EntryModelQuerySet(self.model, using=self._db)

		def search(self, query=None):
			return self.get_queryset().search(query=query)


	title 								= models.CharField(verbose_name="title", max_length=50, null=False, blank=False)
	code 								= models.CharField(verbose_name="code", max_length=15, null=False, blank=False)

	price_market_triggers				= ArrayField(
											models.CharField(max_length=125),
											size=10, null=False, blank=False
										)


	timestamp							= models.DateTimeField(auto_now_add=True)

	objects = EntryModelManager()


	def __str__(self):
		return f"{self.id}"
		

	def update(self, **kwargs):
		EntryModel.objects.filter(id=self.id).update(**kwargs)
		return EntryModel.objects.get(id=self.id)