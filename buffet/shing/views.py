from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import tushare as ts
from stock import StockBase

# Create your views here.
def index(request):
    if request.method == 'GET':
    	df = ts.get_stock_basics()
    	print df.size
    	st = df[0:1]
    	name = st['name'][0]
    	code = st['name'].axes[0][0]
    	industry = st['industry'][0]
    	area = st['area'][0]
    	pe = st['pe'][0]
    	outstanding = st['outstanding'][0]
    	totals = st['totals'][0]
    	totalAssets = st['totalAssets'][0]
    	stb = StockBase(code, name, industry, area, pe, outstanding, totals, totalAssets)
    	nm = stb.getName()
    	print 'name is ' + nm
    	cd = stb.getCode()
    	print 'code is ' + cd 
    	context_dict = {'code': cd}
    	return render(request, 'index.html', context_dict)
        #return HttpResponse("Hello Buffet")
    else:
        print ("get post")
        return JsonResponse({'foo':'bar'})