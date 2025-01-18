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


class JournalQuerySet(models.QuerySet):
	
	def search(self, query=None):
		if query == None:
			return self.none()
		lookups += Q(Q(title__icontains=query) | Q(code__icontains=query))
		return self.filter(lookups)

class Journal(models.Model):
	
	class JournalManager(models.Manager):

		def create(self, title, code, target_profile=None, adages=None):
			model = self.model(
				title=title,
				code=code,
				target_profile=target_profile,
				adages=adages,
			)
			model.save(using=self._db)
			return model

		def get_queryset(self):
			return JournalQuerySet(self.model, using=self._db)

		def search(self, query=None):
			return self.get_queryset().search(query=query)


	title 						= models.CharField(verbose_name="title", max_length=125, null=False, blank=False)
	code						= models.CharField(verbose_name="code", max_length=15, unique=True, null=False, blank=False)

	target_profile 				= models.ManyToManyField(
		"trading_plan.ObjectiveProfile",
		related_name="trading_plans",
		related_query_name="trading_plan",
		blank=True,
	)

	adages 						= ArrayField(models.CharField(max_length=125,null=True, blank=True), size=5, null=True, blank=True)

	timestamp					= models.DateTimeField(auto_now_add=True)


	objects = JournalManager()


	def __str__(self):
		return f"{self.id}"

	def update(self, **kwargs):
		Journal.objects.filter(id=self.id).update(**kwargs)
		return Journal.objects.get(id=self.id)


class TradingModelQuerySet(models.QuerySet):
	
	def search(self, query=None):
		if query == None:
			return self.none()
		lookups += Q(Q(positive_price_market_signatures__icontains=query))
		return self.filter(lookups)

class TradingModel(models.Model):
	
	class TradingModelManager(models.Manager):

		def create(self,
				market_conditions,
				preffered_days, preffered_session, preffered_hour,
				positive_price_market_signatures, negative_price_market_signatures,
				trading_style,
				risk_appetite, riskreward_profile, avg_duration,
				win_rate, breakeven_rate, reversal_rate, avg_return, avg_loss,
				routines=None
			):
			model = self.model(
				market_conditions=market_conditions,
				preffered_days=preffered_days,
				preffered_session=preffered_session,
				preffered_hour=preffered_hour,
				positive_price_market_signatures=positive_price_market_signatures,
				negative_price_market_signatures=negative_price_market_signatures,
				trading_style=trading_style,
				routines=routines,
				risk_appetite=risk_appetite,
				riskreward_profile=riskreward_profile,
				avg_duration=avg_duration,
				win_rate=win_rate,
				breakeven_rate=breakeven_rate,
				reversal_rate=reversal_rate,
				avg_return=avg_return,
				avg_loss=avg_loss,
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

	trading_style 						= models.CharField(verbose_name="trading_style", choices=TradingStyles.choices, default=TradingStyles.DAY_TRADING, max_length=3, null=False, blank=False)
	
	routines 							= models.ManyToManyField(
		"tasks.Routine",
		related_name="trading_models",
		related_query_name="trading_model",
		blank=True,
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