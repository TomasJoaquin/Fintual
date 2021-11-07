import datetime
import random

class Portfolio:

	def __init__(self, stocks):
		self.stocks = stocks

	def profit(self, init_date, end_date):
		init_value = 0
		end_value = 0
		for stock in self.stocks:
			init_value += stock.price(init_date)
			end_value += stock.price(end_date)
		profit = (end_value-init_value)/init_value
		return profit

	def anualized_profit(self, init_date, end_date):
		init_value = 0
		end_value = 0
		for stock in self.stocks:
			init_value += stock.price(init_date)
			end_value += stock.price(end_date)
		delta_days = (end_date - init_date).days
		anualized_profit = ((end_value/init_value)-1)**(1/float(delta_days))
		return anualized_profit		


class Stock:

	def __init__(self, name, prices):
		self.name = name
		self.prices = prices

	def price(self, date):
		if date in self.prices:
			return self.prices[date]
		else:
			return "Unknown value for {}".format(date.strftime("%d/%m/%Y"))


def test(n_stocks, initial_stock_value, test_init_date, test_end_date):
	testing_stocks = []
	for i in range(n_stocks):
		stock_name = "Accion {}".format(i)
		stock_prices = dict()

		dates = []
		init_date = test_init_date
		stock_value = initial_stock_value

		while init_date < test_end_date:
			dates.append(init_date)
			stock_value += random.random()
			stock_prices[init_date] = stock_value
			init_date += datetime.timedelta(days=1)

		testing_stocks.append(Stock(stock_name, stock_prices))

	testing_portfolio = Portfolio(testing_stocks)
	print(testing_portfolio.profit(test_init_date, test_end_date - datetime.timedelta(days=1)))
	print(testing_portfolio.anualized_profit(test_init_date, test_end_date - datetime.timedelta(days=1)))


# Uncomment this call to test the code
#test(6, 1000, datetime.date(2020, 12, 1), datetime.date(2021, 1, 1))