from django.shortcuts import render
from django.http import HttpResponse


def calc(request):

	return render(request, 'test.html')

def operator(request):
	x = request.GET['operator']
	y = request.GET['number1']
	z = request.GET['number2']
	if x == 'sum':
		return render(request, 'test.html', {'result': float(y)+float(z)})
	elif x == 'subtract':
		return render(request, 'test.html', {'result': float(y)-float(z)})
	elif x == 'multiply':
		return render(request, 'test.html', {'result': float(y)*float(z)})
	elif x == 'divide':
		return render(request, 'test.html', {'result': float(y)/float(z)})

