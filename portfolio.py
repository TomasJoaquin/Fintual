import datetime
import random


class Portfolio:
	"""
	Clase que contiene información relativa a un portafolio (financiero) determinada

	Parameters:
	stocks ([Stock]): lista de acciones (objetos Stock).
	"""

	def __init__(self, stocks):
		self.stocks = stocks

	def profit(self, init_date, end_date):
		"""
		Retorna la rentabilidad de un portafolio (en formato 0.) entre dos fechas dadas

		Parameters:
		init_date (datetime.date): fecha inicial del período de análisis
		end_date (datetime.date): fecha de término del período de análisis

		Returns:
		float: porcentaje de rentabilidad del portafolio entre las fechas ingresadas
		"""
		init_value = 0
		end_value = 0
		for stock in self.stocks:
			init_value += stock.price(init_date)
			end_value += stock.price(end_date)
		profit = (end_value-init_value)/init_value
		return profit

	def anualized_profit(self, init_date, end_date):
		"""
		Retorna la rentabilidad anualizada de un portafolio (en formato 0.) entre dos fechas dadas

		Parameters:
		init_date (datetime.date): fecha inicial del período de análisis
		end_date (datetime.date): fecha de término del período de análisis

		Returns:
		float: porcentaje de rentabilidad del portafolio entre las fechas ingresadas
		"""
		init_value = 0
		end_value = 0
		for stock in self.stocks:
			init_value += stock.price(init_date)
			end_value += stock.price(end_date)
		delta_days = (end_date - init_date).days
		anualized_profit = ((end_value/init_value)-1)**(1/float(delta_days))
		return anualized_profit		


class Stock:
	"""
	Clase que contiene información relativa a una acción (financiera) determinada

	Parameters:
	name (str): nombre de la acción
	prices (dict(datetime.date, float)): diccionario que contiene el precio de la acción en determinadas fechas. Sus llaves son fechas, y el valor asociado a cada llave es el precio de la acción en dicha fecha.
	"""

	def __init__(self, name, prices):
		self.name = name
		self.prices = prices

	def price(self, date):
		"""
		Retorna el valor de la acción en una fecha determinada

		Parameters:
		date (datetime.date): fecha en la cual se quiere conocer el valor de la acción

		Returns:
		int/string: el valor de la acción en la fecha ingresada o un string en el caso de que no haya datos sobre dicha fecha
		"""
		if date in self.prices:
			return self.prices[date]
		else:
			return "Unknown value for {}".format(date.strftime("%d/%m/%Y"))


def test(n_stocks, initial_stock_value, test_init_date, test_end_date):
	"""
	Función implementada para testear las clases Stock y Portfolio. Crea una serie de acciones (Stock) con valores dummy, para luego crear un objeto Portfolio que las contenga.
	Finalmente imprime la rentabilidad y la rentabilidad anualizada del portafolio durante las fechas que se ingresen.

	Parameters:
	n_stocks (int): numero de acciones que se generarán para añadir al portafolio
	initial_stock_value (float): valor inicial de las acciones
	test_init_date (datetime.date): fecha de inicio del período que se quiera testear
	test_end_date (datetime.date): fecha de término del período que se quiera testear
	"""
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
	print("Rentabilidad del Portafolio de prueba: {}".format(testing_portfolio.profit(test_init_date, test_end_date - datetime.timedelta(days=1))))
	print("Rentabilidad anualizada del Portfolio de prueba: {}".format(testing_portfolio.anualized_profit(test_init_date, test_end_date - datetime.timedelta(days=1))))


# Descomentar esta línea para testear el código :D
#test(6, 1000, datetime.date(2020, 12, 1), datetime.date(2021, 1, 1))


"""
Quise programar la clase Stock y una función de testing a fin de poder probar que mi código funcionase :)
No sabía que era la rentabilidad anualizada, así que investigué un poco y utilicé la fórmula que encontré en https://www.gestionpasiva.com/como-calcular-rentabilidad-anualizada-inversion/ (perdón si no era esa D:)
"""