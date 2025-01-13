from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class Genders(TextChoices):
	MALE = "MLE", _("Male")
	FEMALE = "FML", _("Female")
	NON_BINARY = "NBN", _("Non-binary")


# = = = Trading plan

class TradingStyles(TextChoices):
	SHORT_TERM = "STT", _("Short term")
	MEDIUM_TERM = "MTT", _("Medium term")
	LONG_TERM = "LTT", _("Long term")

	SWING_TRADING = "SWI", _("Swing trading")
	SCALPING = "SCP", _("Scalping")
	DAY_TRADING = "DYT", _("Day trading")

class Markets(TextChoices):
	COMMODITIES = "COM", _("Commodities")
	FUTURES = "FUT", _("Futures")
	DERIVATIVES = "DRV", _("Derivatives")
	FOREX = "FOX", _("Forex")

class GeneralMarketConditions(TextChoices):
	BULLISH = "BUL", _("Bullish")
	BEARISH = "BER", _("Bearish")
	CONSOLIDATING = "CON", _("Consolidating")
	RETRACEMENT = "RET", _("Retracement")

class TradingDays(TextChoices):
	MONDAY = "MON", _("Monday")
	TUESDAY = "TUE", _("Tuesday")
	WEDNESDAY = "WED", ("Wednesday")

class TradingHours(TextChoices):
	HOUR_1 = "HR1", _("01:00")
	HOUR_2 = "HR2", _("02:00")
	HOUR_3 = "HR3", _("03:00")
	HOUR_4 = "HR4", _("04:00")
	HOUR_5 = "HR5", _("05:00")

class TradingSessions(TextChoices):
	LONDON = "LON", _("London")
	ASIA = "ASI", _("Asia")
	NEW_YORK = "NYC", _("New York")

class RiskAppetites(TextChoices):
	HIGH = "HIG", _("High")
	MEDIUM = "MED", _("Medium")
	LOW = "LOW", _("Low")

class RiskRewardProfiles(TextChoices):
	ONE_TWO = "OTT", _("1:2")
	ONE_THREE = "OTR", _("1:3")
	ONE_FOUR = "OTF", _("1:4")

class OrderTypes(TextChoices):
	BUY = "BUY", _("Buy")
	SELL = "SEL", _("Sell")
	SELL_LIMIT = "SLL", _("Sell limit")
	BUY_LIMIT = "BYL", _("Buy limit")

class TradeOutcomes(TextChoices):
	IN_PROGRESS = "INP", _("In progress")
	WIN = "WIN", _("Win")
	LOSS = "LOS", _("Loss")

# = = = Tasks

class TaskStates(TextChoices):
	NOT_DONE = "NTD", _("Not done")
	DONE = "DON", _("Done")
	IN_PROGRESS = "INP", _("In progress")