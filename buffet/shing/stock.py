class StockBase(object):
	"""The stock class"""
	def __init__(self, code, name, industry, area, pe, outstanding, totals, totalAssets):
		self.code = code
		self.name = name
		self.industry = industry
		self.area = area
		self.pe = pe
		self.outstanding = outstanding
		self.totals = totals
		self.totalAssets = totalAssets

	def getPE(self):
		return sefl.pe

	def getCode(self):
		return self.code

	def getName(self):
		return self.name


class Stock(StockBase):
	"""docstring for Stock"""
	def __init__(self, code, name, industry, area, pe, outstanding, totals, totalAssets, price):
		super().__init__(code, name, industry, area, pe, outstanding, totals, totalAssets)
		self.price = price

	def getPrice():
		return self.price
		