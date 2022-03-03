from django.shortcuts import render
from django.http import HttpResponse
def calculate(request,calc):
	try:
		result=eval(calc)
	except:
		return HttpResponse("<html>La expresion dada no es una expresion valida</html>")
	return render(request,"calculate.html",{"comb":calc,"eval":str(result)})
