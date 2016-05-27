from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import tushare as ts

# Create your views here.
def index(request):
    if request.method == 'GET':
    	df = ts.get_stock_basics()
    	print df.size
    	return render(request, 'index.html')
        #return HttpResponse("Hello Buffet")
    else:
        print ("get post")
        return JsonResponse({'foo':'bar'})