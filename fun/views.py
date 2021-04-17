from django.shortcuts import render
import pyjokes

# Create your views here.

def index(request):
	joke = pyjokes.get_joke()
	context = {"joke" : joke}
	return render(request, "fun/index.html", context)